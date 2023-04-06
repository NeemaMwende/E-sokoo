from contextvars import Context
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from sokoapp.models import Product
from django.contrib import messages
from django.views import generic
from .models import OrderItem
from sokoapp.forms import *
from .cart import Cart
from .forms import *
import stripe
from django.conf import settings
from django.urls import reverse
# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY



class CheckoutSession(generic.View):
  def post(self,request, *args, **kwargs):

    host = self.request.get_host()
    payment_method_type=['card'],

    checkout_session = stripe.checkout.Session.create(
            line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'e soko products',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://{}{}'.format(host,reverse('cart:success')),
    cancel_url='http://{}{}'.format(host,reverse('cart:cancel')),

    )
    return redirect(checkout_session.url, code=303)

def Success(request):
    context ={

        'payment':'success'
    }
 
    return render(request, 'cart/success.html',context)

def Cancel(request):
    context ={

        'payment':'succ'
    }
    return render(request, 'cart/success.html',context)


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request,f'Your item was added to the cart successfully.')
    return redirect('product_list')

def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('product_list')
    
@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})


def checkout(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            messages.success(request,f'Your order was successfully processed.')
        return render(request, 'cart/ordered.html', {'order': order,'cart': cart})
    else:
        form = OrderCreateForm()
    return render(request, 'cart/order.html', {'form': form,'cart': cart})

