from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from cart.forms import CartAddProductForm
from django.contrib import messages
from .emails import send_welcome_email
from sokoapp.models import Product
from .forms import *
from .models import *
from .cart import *


def home(request):
 
    return render(request, 'home.html')

@login_required
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

    
def shop(request):
   products = Product.objects.all
   if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('shop')
            print('valid')
        else:
         form = NewsLetterForm()
   return render(request,"shop.html",{'products':products})

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
         messages.success(request,f"Hi { username }, your account has been created successfully!")
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













