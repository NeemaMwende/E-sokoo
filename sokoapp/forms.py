from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email')



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['first_name', 'last_name', 'email','Country', 'city', 'address', 'postal_code','zip']

