from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Cloth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cloth/')
    description = HTMLField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
   
    def __str__(self):
        return self.name
