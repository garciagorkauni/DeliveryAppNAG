from django import forms
from .models import Profile, Address
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('email', 'name', 'surname', 'birthdate', 'telephone')

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=['name','surname', 'telephone', 'country', 'postal_code', 'city', 'address1', 'address2']