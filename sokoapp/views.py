from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.contrib import messages
from .emails import send_welcome_email
from sokoapp.models import Product
from .forms import *
from .models import *
from .cart import *
import requests
from django.views import generic
from .forms import *
from django.contrib import messages
import stripe
from django.conf import settings
from django.urls import reverse
from contextvars import Context
import re
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
 
    return render(request, 'home.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()[::-1]
    products = Product.objects.filter(available=True)[::-1]
    cart_product_form = CartAddProductForm()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'product.html', context)


def send_welcome_email(name, email):
    subject = 'Welcome to My Newsletter!'
    body = f"Hi {name},\n\nThanks for subscribing to my newsletter. I'll be sending you regular updates on my latest projects and articles.\n\nBest regards,\nJohn Doe"

    return requests.post(
        f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": "John Doe <john@example.com>",
              "to": email,
              "subject": subject,
              "text": body})


def home(request):

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('home')
            print('valid')
    else:
        form = NewsLetterForm()

    return render(request, "home.html", {'Form': form})

def women(request):
     if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('women')
            print('valid')
     else:
        form = NewsLetterForm()
     return render(request, "women.html", {'Form': form})

def men(request):
     if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('men')
            print('valid')
     else:
        form = NewsLetterForm()
     return render(request, "men.html", {'Form': form})

    
def about(request):
     if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('about')
            print('valid')
     else:
        form = NewsLetterForm()
     return render(request, "about.html", {'Form': form})


def signup(request):
    if request.method=="POST":
     form=SignupForm(request.POST)
     if form.is_valid():
         form.save()
         username= form.cleaned_data["username"]
         email = form.cleaned_data['email']
      

        #  recipient = SignupForm(username=username, email=email)
        #  recipient.save()
         send_welcome_email(username,email) 
         
         return redirect("login")
    else:
         form=SignupForm()
         
   
    return render(request,"registration/signup.html",{'form':form})

@login_required
def profile(request):
     if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('profile')
            print('valid')
     else:
        form = NewsLetterForm()
     return render(request,"registration/profile.html",)







# cart views

class CheckoutSession(generic.View):
  def post(self,request, *args, **kwargs):

    host = self.request.get_host()
    payment_method_type=['card'],

    checkout_session = stripe.checkout.Session.create(
            line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'e soko products',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://{}{}'.format(host,reverse('cart:success')),
    cancel_url='http://{}{}'.format(host,reverse('cart:cancel')),

    )
    return redirect(checkout_session.url, code=303)

def Success(request):
    context ={

        'payment':'success'
    }
 
    return render(request, 'cart/success.html',context)

def Cancel(request):
    context ={

        'payment':'succ'
    }
    return render(request, 'cart/success.html',context)


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request,f'Your item was added to the cart successfully.')
    return redirect('product_list')

def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('product_list')
    
@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})


def checkout(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            messages.success(request,f'Your order was successfully processed.')
        return render(request, 'cart/ordered.html', {'order': order,'cart': cart})
    else:
        form = OrderCreateForm()
    return render(request, 'cart/order.html', {'form': form,'cart': cart})



