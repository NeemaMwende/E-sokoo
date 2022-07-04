from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
  
def women(request):
    return render(request,"women.html")
def men(request):
    return render(request,"men.html")
def shop(request):
    return render(request,"shop.html")
def about(request):
    return render(request,"about.html")