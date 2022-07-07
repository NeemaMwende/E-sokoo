from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url('^add/(\d+)/', views.cart_add, name='cart_add'),
    url('^remove/(\d+)/', views.cart_remove, name='cart_remove'),
    
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)