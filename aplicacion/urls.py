from django.urls import path, include

from .views import añadirProducto, busqueda, carrito, dashboard, editarProducto, exito, index, info_producto, infoUsuario, listaClientes, listaProductos, login, pago, productos, registro, ventas

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
    path('dashboard/usuario', infoUsuario, name='usuario'),
    path('dashboard/productos', listaProductos, name='productos'),
    path('dashboard/ventas', ventas, name='ventas'),
]
