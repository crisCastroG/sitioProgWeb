from django.contrib import admin

from aplicacion.models import CarroCompra, Cliente, Pedido, Producto, ProductoCarro

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(CarroCompra)
admin.site.register(ProductoCarro)