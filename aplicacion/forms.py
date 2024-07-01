from django import forms
from .models import Cliente, Producto, Pedidos
from django.contrib.auth.forms import UserCreationForm


class UpdClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre','email','direccion','imagen']

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
    pass



class UpdVentaForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['estado_pedido']
