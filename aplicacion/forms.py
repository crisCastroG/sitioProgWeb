from django import forms
from .models import Cliente, Producto


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
