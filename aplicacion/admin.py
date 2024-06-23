from django.contrib import admin

from aplicacion.models import CarroCompra, Cliente, Pedidos, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedidos)
admin.site.register(CarroCompra)