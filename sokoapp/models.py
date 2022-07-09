from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=100, null=True)
    photo = models.ImageField(upload_to='product/',blank=True)

    description = HTMLField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
   
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


    price = models.IntegerField()
    available = models.BooleanField(default=True)
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name
    

