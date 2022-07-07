from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('sokoapp.urls')),
    
]

admin.site.site_header= "Soko Administration"
admin.site.site_title="SOKO"
