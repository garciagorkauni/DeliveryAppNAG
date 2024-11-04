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

class PaymentForm(forms.Form):
    address = forms.ChoiceField(label="Select Address", choices=[])

    def __init__(self, *args, profile=None, **kwargs):
        super().__init__(*args, **kwargs)
        if profile:
            self.fields['address'].choices = [
                (address.address_id, f"{address.address1}, {address.city}, {address.country}")
                for address in Address.objects.filter(profile=profile)
            ]