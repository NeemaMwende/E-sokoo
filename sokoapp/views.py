from string import Template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
# Create your views here.



def home(request):
    clothes = Product.objects.all
    return render(request, 'home.html',{'clothes':clothes})

def women(request):
    return render(request,"women.html")
def men(request):
    return render(request,"men.html")
    
def shop(request):
   clothes = Product.objects.all
   return render(request,"shop.html",{'clothes':clothes})

class addToCart(TemplateView):
    template_name = "cart.html"
    # Get product by id


    # get product

    # check if cart exists

    # check if product is already exists
 
  

def about(request):
    return render(request,"about.html")

def signup(request):
    if request.method=="POST":
     form=UserCreationForm(request.POST)
     if form.is_valid():
         form.save()
         username= form.cleaned_data["username"]
         messages.success(request,f"Hi { username }, your account has been created successfully!")
         return redirect("home")
    else:
         form=UserCreationForm()
         
   
    return render(request,"registration/signup.html",{'form':form})
