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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].label = 'Pasahitza'
        self.fields['password2'].label = 'Pasahitza Konfirmazioa'
        # Añadir clases personalizadas a los campos del modelo Profile
        for field_name in self.fields:
            if field_name == 'email':
        # Personaliza solo el campo 'email'
                self.fields['email'].widget.attrs.update({
                    'class': 'mi-estilo-input-email',  # clase específica para email si deseas
                    'placeholder': 'Sartu zure posta helbidea'  # placeholder específico para email
                })
            elif  field_name in ['password1', 'password2']:
                # Aplica clase y placeholder solo a password1 y password2
                self.fields['password1'].widget.attrs.update({
                    'class': 'mi-estilo-input',
                    'placeholder': 'Sartu zure pasahitza'
                })
                self.fields['password2'].widget.attrs.update({
                    'class': 'mi-estilo-input',
                    'placeholder': 'Pasahitza konfirmatu'
                })
            else:
              
                # Aplica clase a los otros campos
                self.fields[field_name].widget.attrs.update({
                    'class': 'mi-estilo-input',
                    'placeholder': f'Sartu zure {self.fields[field_name].label.lower()}'
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