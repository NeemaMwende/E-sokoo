from multiprocessing import context
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

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        # Get product by id
        product_id = self.kwargs['pro_id']

        # get product
        product_obj = Product.objects.get(id=product_id)

        # check if cart exists
        cart_id= self.request.session.get('cart_id', None)
        if cart_id:
            cart_odj= Cart.objects.get(id=cart_id)    
            this_product_in_cart=cart_odj.CartProduct_set.filter('product')
        else:
            cart_obj= Cart.objects.create(total=0)
            self.request.session["cart_id"]=cart_obj.id
       
         

        # check if product is already exists
        


        return context
   
  

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
