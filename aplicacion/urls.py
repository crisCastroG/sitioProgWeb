from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import añadirProducto, busqueda, carrito, dashboard, editarProducto, exito, index, info_producto, infoUsuario, listaClientes, listaProductos, login, pago, productos, registro, ventas, modificarCliente, eliminarCliente

urlpatterns = [
    #URLS DE APLICACION
    path('', index, name='index'),
    path('busqueda/',busqueda, name='busqueda'),
    path('carrito/',carrito, name='carrito'),
    path('exito/',exito, name='exito'),
    path('info_producto/',info_producto, name='info_producto'),
    path('login/',login, name='login'),
    path('pago/',pago, name='pago'),
    path('productos/',productos, name='productos'),
    path('registro/',registro, name='registro'),
    #URLS DE DASHBOARD
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/añadir', añadirProducto, name='añadir'),
    path('dashboard/cliente', listaClientes, name='cliente'),
    path('dashboard/editar', editarProducto, name='editar'),
    path('dashboard/usuario/<id>', infoUsuario, name='usuario'),
    path('dashboard/productos', listaProductos, name='productos'),
    path('dashboard/ventas', ventas, name='ventas'),
    path('dashboard/modificar/<id>', modificarCliente, name='modificar'),
    path('dashboard/eliminar/<id>', eliminarCliente, name='eliminar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)