from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
 
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('addToCart/<int:pk>', addToCart, name='addToCart'),
    # path('cartView/', cartView, name='cartView'),
    path('women/', women, name='women'),
    path('men/', men, name='men'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('products/', views.product_list, name='product_list'),
    path('productCategory/<category_slug>', views.product_list, name='productCategory'),
    path('productDetail/', views.product_detail, name='product_detail'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)