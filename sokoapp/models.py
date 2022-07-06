from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product/')
    description = HTMLField()
    price = models.IntegerField()


    def __str__(self):
        return self.name


 
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "cart: " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "cart: " + str(self.cart.id) + "CartProduct: " + str(self.id)
        
        