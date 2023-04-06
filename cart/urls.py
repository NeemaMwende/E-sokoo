from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views
from .views import *

app_name = 'cart'
urlpatterns = [
    url('^$', views.cart_detail, name='cart_detail'),
    url('add/(\d+)/', views.cart_add, name='cart_add'),
    url('remove/(\d+)/', views.cart_remove, name='cart_remove'),
    url('checkout/', views.checkout, name='checkout'),
    url('CheckoutSession/', CheckoutSession.as_view(), name='CheckoutSession'),
    url('success/', views.Success, name='success'),
    url('cancel/', views.Cancel, name='cancel'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)