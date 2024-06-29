from django.db import models

from aplicacion.enumeraciones import ESTADO_PEDIDO

# Create your models here.
class Cliente(models.Model):
    imagen=models.ImageField(upload_to='personas', null=True)
    rut=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    email=models.EmailField(verbose_name='E-mail')
    direccion=models.CharField(max_length=500, null=False)

class Producto(models.Model):
    codigo=models.CharField(max_length=10, primary_key=True, null=False)
    foto_pro=models.ImageField(upload_to='productos',null=False)
    precio=models.CharField(max_length=9,null=False)
    nombre_pro=models.CharField(max_length=100, null=False)
    descripcion=models.CharField( max_length=100, null=False)
    stock=models.CharField(max_length=5,null=False)

class Pedidos(models.Model):
    nro_pedido=models.CharField(max_length=10, primary_key=True, null=False)
    rut_cli=models.ForeignKey(Cliente,on_delete=models.PROTECT)
    #correo_pe=models.ForeignKey(Cliente,on_delete=models.PROTECT)
    #resumen_pe=models.CharField(Cliente,on_delete=models.PROTECT)
    fecha_pedido = models.DateField(null=False)
    estado_pedido=models.CharField(default='Pendiente', max_length=10, null=False, choices=ESTADO_PEDIDO)

class CarroCompra(models.Model):
    nro_carro=models.CharField(max_length=10, primary_key=True, null=False)
    rut_cli=models.ForeignKey(Cliente,on_delete=models.PROTECT)