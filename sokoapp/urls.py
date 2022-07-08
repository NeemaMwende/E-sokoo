from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  
    url('', views.home, name='home'),
    url('womens/', views.women, name='women'),
    url('men/', views.men, name='men'),
    url('shop/', views.shop, name='shop'),
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)