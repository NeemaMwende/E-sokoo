from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('signup/', views.signup, name='signup'),
    path('products/', views.product_list, name='product_list'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path('cart/checkout/', views.checkout, name='checkout'),
# path('cart/CheckoutSession/', CheckoutSession.as_view(), name='CheckoutSession'),
    path('cart/success/', views.Success, name='success'),
    path('cart/cancel/', views.Cancel, name='cancel'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
