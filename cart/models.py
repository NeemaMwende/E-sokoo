from django_countries.fields import CountryField
from django.contrib.auth.models import User
from sokoapp.models import Product
from django.db import models



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