from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    # path('checkout/', include('checkout.urls')),
    path('', include('sokoapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    
]

admin.site.site_header= "Soko Administration"
admin.site.site_title="SOKO"

