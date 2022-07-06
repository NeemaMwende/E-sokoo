from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cart/', views.addToCart, name='cart'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)