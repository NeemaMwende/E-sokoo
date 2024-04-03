from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
    path('', include('sokoapp.urls')),  # Include sokoapp URLs without namespace
    path('cart/', include(('sokoapp.urls', 'sokoapp'), namespace='cart')), 
    
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header = "Soko Administration"
admin.site.site_title = "SOKO"
