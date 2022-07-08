
from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from sokoapp.forms import NewsLetterForm
from sokoapp.models import NewsLetterRecipients
from .emails import send_welcome_email
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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





# Create your views here.

  
def women(request):
    return render(request,"women.html")


def men(request):
    return render(request,"men.html")


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

# def photo_category(request, category_photo):
#     images = PhotoImage.filter_by_location(location)
#     print(images)
#     return render(request, '.html', {'category_images': images})