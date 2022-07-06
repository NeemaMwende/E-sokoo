from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    clothes = Cloth.objects.all
    return render(request, 'home.html', {"clothes": clothes})

def women(request):
    return render(request,"women.html")
def men(request):
    return render(request,"men.html")
    
def shop(request):
    clothes = Cloth.objects.all
    return render(request,"shop.html",{"clothes": clothes})

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
