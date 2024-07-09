from django import forms
from aplicacion.validator import validar_rut
from .models import Cliente, Pedido, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class RUTField(forms.CharField):
    default_error_messages = {
        'invalid': 'El RUT ingresado no es válido. Debe ser sin puntos y guión',
    }

    def clean(self, value):
        value = super().clean(value)
        if not validar_rut(value):
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value

class UpdClienteForm(forms.ModelForm):
    rut = RUTField(label='RUT', max_length=12, required=True)
    nombre = forms.CharField(required=True, min_length=3, max_length=100)
    direccion = forms.CharField(required=True, min_length=3, max_length=200)

    def clean_codigo(self):
        rut = self.cleaned_data["rut"]
        existe = Cliente.objects.filter(rut = rut).exists()
        if existe:
            raise ValidationError("Este rut ya existe en el sistema")
        return rut
    
    class Meta:
        model = Cliente
        fields = ['nombre','rut','direccion']

class ProductoForm(forms.ModelForm):   
    codigo=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese codigo"}, 
                        help_text="Debe ingresar un codigo")
    
    def clean_codigo(self):
        codigo = self.cleaned_data["codigo"]
        existe = Producto.objects.filter(codigo = codigo).exists()
        if existe:
            raise ValidationError("Este codigo de producto ya existe")
        return codigo
    
    class Meta:
        model = Producto
        fields = ['codigo','foto_pro','precio', 'nombre_pro','descripcion', 'stock']


class UpdProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['foto_pro','precio','nombre_pro','categoria','descripcion', 'stock']

class CustomCreationForm(UserCreationForm):

    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        existe = Cliente.objects.filter(email = email).exists()

        if existe:
            raise ValidationError("Este email ya está registrado")
        return email
    
    class Meta:
        model = User
        fields = ['username',"email","password1","password2"]
    

class UpdVentaForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado_pedido']



