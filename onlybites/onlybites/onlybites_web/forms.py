from django import forms
from .models import Profile, Address
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('email', 'name', 'surname', 'birthdate', 'telephone', 'password1', 'password2')
        labels = {
            'email': 'Posta Helbidea',
            'name': 'Izena',
            'surname': 'Abizena',
            'birthdate': 'Jaiotze Data',
            'telephone': 'Telefono Zenbakia',
          

        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'mi-estilo-input-email', 'placeholder': 'Sartu zure helbide elektronikoa'}),
            'name': forms.TextInput(attrs={'class': 'mi-estilo-input', 'placeholder': 'Sartu zure izena'}),
            'surname': forms.TextInput(attrs={'class': 'mi-estilo-input', 'placeholder': 'Sartu zure abizena'}),
            'birthdate': forms.DateInput(attrs={'class': 'mi-estilo-input', 'type': 'date', 'placeholder': 'Sartu jaiotze data'}),
            'telephone': forms.TextInput(attrs={'class': 'mi-estilo-input', 'placeholder': '+34'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].label = 'Pasahitza'
        self.fields['password2'].label = 'Pasahitza Baieztatu'
        # Añadir clases personalizadas a los campos del modelo Profile
        for field_name in self.fields:
        
            if  field_name in ['password1', 'password2']:
                # Aplica clase y placeholder solo a password1 y password2
                self.fields['password1'].widget.attrs.update({
                    'class': 'mi-estilo-input',
                    'placeholder': 'Sartu zure pasahitza'
                })
                self.fields['password2'].widget.attrs.update({
                    'class': 'mi-estilo-input',
                    'placeholder': 'Pasahitza baieztatu'
                })
         
    
class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=['name','surname', 'telephone', 'country', 'postal_code', 'city', 'address1', 'address2']

        labels = {
            'name': 'Izena',
            'surname': 'Abizena',
            'telephone': 'Telefono Zenbakia',
            'country': 'Herrialdea',
            'postal_code': 'Posta Helbidea',
            'city': 'Hiria',
            'address1': 'Helbidea',
            'address1': 'Helbidea 2',
        }
        