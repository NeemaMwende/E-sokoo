from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Cloth(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cloth/')
    description = HTMLField()
    price = models.IntegerField()
   
    def __str__(self):
        return self.name

class orderItem(models.Model):
    item = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(orderItem)
    date = models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
  
   
    def __str__(self):
        return self.user