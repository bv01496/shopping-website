from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Contact
from products.models import Address
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = False)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'id':'signupusername','autocomplete':'on'})
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','issue']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['location','street','pincode','phonenumber']
        widgits = {
            'location' : forms.TextInput(attrs={'name':'location','required':'True'}),
            'street' : forms.TextInput(attrs={'name':'street','required':'True'}),
            'pincode' : forms.TextInput(attrs={'name':'pincode','required':'True'}),
            'phonenumber' : forms.TextInput(attrs={'name':'phonenumber','required':'True'}),
        }