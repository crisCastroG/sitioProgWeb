from django import forms
from .models import Cliente


class UpdClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre','email','direccion','imagen']