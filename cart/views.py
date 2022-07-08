from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from sokoapp.models import Product
from .cart import Cart
from .forms import *
from sokoapp.forms import *
from sokoapp.models import NewsLetterRecipients
from sokoapp.emails import send_welcome_email
from django.http import HttpResponse, Http404, HttpResponseRedirect



@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('product_list')

def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('product_list')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'detail.html', {'cart': cart})

def details(request):

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('detail')
            print('valid')
    else:
        form = NewsLetterForm()

    return render(request, "detail.html", {'Form': form})
