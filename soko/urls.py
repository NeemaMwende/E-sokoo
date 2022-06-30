from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('community.urls')),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header= "Soko Administration"
admin.site.site_title="SOKO"
