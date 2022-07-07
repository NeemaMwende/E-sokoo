from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm
from django.contrib import messages
from sokoapp.models import Product
from .forms import *
from .models import *
from .cart import *


def home(request):
    products = Product.objects.all
    return render(request, 'home.html',{'products':products})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'list.html', context)

def women(request):
    return render(request,"women.html")
def men(request):
    return render(request,"men.html")
    
def shop(request):
   products = Product.objects.all
   return render(request,"shop.html",{'products':products})

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






























# def addToCart(request,pk):

#     try:
#         the_id = request.session['cart_id']
#     except:
#         new_cart= Cart()
#         new_cart.save()
#         request.session['cart_id']= new_cart.id
#         the_id=new_cart.id

#     cart= Cart.objects.get(pk=pk)

#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         pass

#     if not product in cart.products.all():
#         cart.products.add(product)
#     else:
#         cart.products.remove(product)

#     new_total= 0.00
#     for item in cart.products.all():
#         new_total += float(item.price)

#     request.session['item_total'] = cart.products.count()
#     cart.total = new_total
#     cart.save()

#     return HttpResponseRedirect(reverse(home))

# class addToCart(TemplateView):


    
#      return render(request,"cartView.html",{'cartView':cartView})

    # template_name = "cart.html"

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)

    #     # Get product by id
    #     product_id = self.kwargs['pro_id']

    #     # get product
    #     product_obj = Product.objects.get(id=product_id)

    #     # check if cart exists
    #     cart_id= self.request.session.get('cart_id', None)
    #     if cart_id:
            
    #         cart_odj= Cart.objects.get(id=cart_id)    
    #         this_product_in_cart=cart_odj.cartproduct_set.filter(product= product_obj)
         
    #         # if items already exists in cart
    #         if this_product_in_cart.exists():
    #             cartproduct = this_product_in_cart.last()
    #             cartproduct.quantity += 1 
    #             cartproduct.subtotal += product_obj.price
    #             cartproduct.save()

    #             cart_obj.total += product_obj.price
    #             cart_obj.save()
    
    #         # item is not available in the cart product,,item is added to cart product
    #         else:
              
    #             cartproduct=CartProduct.objects.create(cart=cart_odj,product=product_obj,quantity=1,subtotal=product_obj.price)
    #             cart_obj.total += product_obj.price
    #             cart_obj.save()
    #     else:
    #         cart_obj= Cart.objects.create(total=0)
    #         self.request.session["cart_id"]=cart_obj.id
    #         cartproduct=CartProduct.objects.create(
    #                 cart=cart_obj,product=product_obj,quantity=1,subtotal=product_obj.price)
    #         cart_obj.total += product_obj.price
    #         cart_obj.save()
       
    #     return context
   
  

# def cartView(request):
#     try:
#         the_id= request.session['cart_id']
#     except:
#         the_id= None
#     if the_id:
#         cart=   Cart.objects.get(id=the_id)
#         context={"cart":cart}
#     else:
#         context={"empty": True}

#     return render(request,"cartView.html",context)

