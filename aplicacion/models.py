from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from aplicacion.enumeraciones import ESTADO_PEDIDO


class Cliente(models.Model):
    email=models.EmailField(primary_key=True, verbose_name='E-mail', null=False)
    rut=models.CharField(max_length=10, null = True)
    nombre=models.CharField(max_length=50, null=True)
    direccion=models.CharField(max_length=500, null=True)
    imagen=models.ImageField(upload_to='personas', null=True)

class Producto(models.Model):
    codigo=models.CharField(max_length=10, primary_key=True, null=False)
    foto_pro=models.ImageField(upload_to='productos',null=False)
    precio=models.CharField(max_length=9,null=False)
    nombre_pro=models.CharField(max_length=100, null=False)
    descripcion=models.CharField( max_length=500, null=False)
    stock=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999)],null=False)

class ProductoCarro(models.Model):
    codigo = models.ForeignKey(Producto, on_delete=models.PROTECT)
    email=models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cantidad_producto = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(250)])
    
class Pedidos(models.Model):
    nro_pedido=models.CharField(max_length=10, primary_key=True, null=False)
    email=models.ForeignKey(Cliente,on_delete=models.PROTECT)
    #correo_pe=models.ForeignKey(Cliente,on_delete=models.PROTECT)
    #resumen_pe=models.CharField(Cliente,on_delete=models.PROTECT)
    fecha_pedido = models.DateField(null=False)
    estado_pedido=models.CharField(default="Pendiente", max_length=10, null=False, choices=ESTADO_PEDIDO)

class CarroCompra(models.Model):
    codigo = models.AutoField(primary_key=True,null=False)
    email = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=False)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999)],null=False)
