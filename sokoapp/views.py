from django.shortcuts import render

from sokoapp.forms import NewsLetterForm

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()

    return render(request,"home.html", {'letterForm': form})


def women(request):
    return render(request,"women.html")


def men(request):
    return render(request,"men.html")


def shop(request):
    return render(request,"shop.html")

