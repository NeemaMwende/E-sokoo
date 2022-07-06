from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product/')
    description = HTMLField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
   
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    date = models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
  
   
    def __str__(self):
        return self.user