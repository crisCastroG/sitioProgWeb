from django import forms
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


def validar_rut(rut: str) -> bool:
    """
    Valida un RUT chileno.
    
    Parámetros:
    rut (str): El RUT a validar, en formato '12345678-9'.

    Retorna:
    bool: True si el RUT es válido, False en caso contrario.
    """
    rut = rut.replace(".", "").upper()
    if not '-' in rut:
        return False
    numero, dv = rut.split("-")
    if not numero.isdigit():
        return False
    numero = int(numero)
    
    def calcular_dv(n: int) -> str:
        suma = 0
        multiplicador = 2
        while n > 0:
            suma += (n % 10) * multiplicador
            n = n // 10
            multiplicador += 1
            if multiplicador == 8:
                multiplicador = 2
        dv = 11 - (suma % 11)
        if dv == 11:
            return '0'
        elif dv == 10:
            return 'K'
        else:
            return str(dv)
    
    return calcular_dv(numero) == dv


class UpdClienteForm(forms.ModelForm):
    rut = RUTField(label='RUT', max_length=12, required=True)
    nombre = forms.CharField(required=True, min_length=3, max_length=100)
    direccion = forms.CharField(required=True, min_length=3, max_length=200)
    class Meta:
        model = Cliente
<<<<<<< HEAD
        fields = ['nombre','email','direccion']
=======

        fields = ['nombre','rut','direccion']
>>>>>>> 8e8e834c5380c21786ac058d4f0bc3ff564b6315

class ProductoForm(forms.ModelForm):   
    codigo=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese codigo"}, 
                        help_text="Debe ingresar un codigo")
    class Meta:
        model = Producto
        fields = ['codigo','foto_pro','precio', 'nombre_pro','descripcion', 'stock']


class UpdProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['foto_pro','precio','nombre_pro','descripcion', 'stock']

class CustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"email","password1","password2"]
    

class UpdVentaForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado_pedido']



