from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home.html")
def women(request):
    return render(request,"women.html")
def men(request):
    return render(request,"men.html")
def shop(request):
    return render(request,"shop.html")
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