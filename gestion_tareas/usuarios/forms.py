from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(forms.ModelForm):
    rol = forms.ChoiceField(choices=Perfil.ROLES)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }