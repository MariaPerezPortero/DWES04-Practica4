from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'tipo', 'requiere_validacion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'requiere_validacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }