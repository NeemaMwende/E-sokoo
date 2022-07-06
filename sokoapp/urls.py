from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('addToCart/<int:pro_id>', addToCart.as_view(), name='addToCart'),
    path('women/', women, name='women'),
    path('men/', men, name='men'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)