from pathlib import Path
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),

    path('products/', views.product_list, name='product_list'),

   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)