from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    clothes = Item.objects.all
    return render(request, 'home.html', {"clothes": clothes})

def women(request):
    return render(request,"women.html")
def men(request):
    return render(request,"men.html")
    
def shop(request):
    clothes = Item.objects.all
    return render(request,"shop.html",{"clothes": clothes})

def addToCart(request,name):
    item = get_object_or_404(Item,name=name)
    orderItem = OrderItem.objects.create(item=item)
    orderQs = Order.objects.filter(user=request.user, ordered=False)

    if orderQs.exists():
        order=orderQs[0]
        #checking if order is already in cart
        if order.items.filter(item__name=item.slug).exists():
            orderItem.quantity += 1
            orderItem.save()


    return render(request,"cart.html")

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
