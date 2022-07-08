from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from sokoapp.forms import NewsLetterForm
from sokoapp.models import NewsLetterRecipients
from .emails import send_welcome_email

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

    return render(request, "home.html", {'letterForm': form})


def women(request):
    return render(request,"women.html")


def men(request):
    return render(request,"men.html")


def shop(request):
    return render(request,"shop.html")

