from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm
from django.contrib import messages
from .forms import NewsLetterForm, SignupForm
from .models import NewsLetterRecipients
from .emails import send_welcome_email

from sokoapp.models import Product
from .forms import *
from .models import *
from .cart import *


def home(request):
    products = Product.objects.all
    return render(request, 'home.html',{'products':products})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
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
    return render(request, 'list.html', context)




# Create your views here.
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
    return render(request,"women.html")


def men(request):
    return render(request,"men.html")

    
def shop(request):
   products = Product.objects.all
   return render(request,"shop.html",{'products':products})

def about(request):
    return render(request,"about.html")




def shop(request):
    
    return render(request,"shop.html")

def about(request):
    return render(request,"about.html")
    

def signup(request):
    if request.method=="POST":
     form=UserCreationForm(request.POST)
     if form.is_valid():
         form.save()
         username= form.cleaned_data["username"]
         messages.success(request,f"Hi { username }, your account has been created successfully!")
         return redirect("login")
    else:
         form=UserCreationForm()
         
   
    return render(request,"registration/signup.html",{'form':form})


def profile(request):
    return render(request,"registration/profile.html",)










# def addToCart(request,pk):

#     try:
#         the_id = request.session['cart_id']
#     except:
#         new_cart= Cart()
#         new_cart.save()
#         request.session['cart_id']= new_cart.id
#         the_id=new_cart.id

#     cart= Cart.objects.get(pk=pk)

#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         pass

#     if not product in cart.products.all():
#         cart.products.add(product)
#     else:
#         cart.products.remove(product)

#     new_total= 0.00
#     for item in cart.products.all():
#         new_total += float(item.price)

#     request.session['item_total'] = cart.products.count()
#     cart.total = new_total
#     cart.save()

#     return HttpResponseRedirect(reverse(home))




