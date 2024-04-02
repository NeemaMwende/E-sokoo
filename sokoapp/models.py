from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django_countries.fields import CountryField

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
    



# cart models

PAYMENT_CHOICES=(

('M-Pesa','M-Pesa'),
('PayPal', 'PayPal'),
('Stripe','Stripe'),

)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    Country = CountryField(blank_label='Select Country',null=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    zip = models.CharField(max_length=30,null=True)
    payment_options = models.BooleanField(default=False,choices=PAYMENT_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity