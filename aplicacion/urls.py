from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import añadirProducto, busqueda, carrito, dashboard, editarProducto, exito, index, info_producto, infoUsuario, listaClientes, listaProductos, login, logout, modificarDatos, modificarPerfil, pago, perfil, categoria, registro, salir, ventas, modificarCliente, eliminarCliente,eliminarProducto,modificarProducto

urlpatterns = [
    #URLS DE APLICACION
    path('', index, name='index'),
    path('busqueda/',busqueda, name='busqueda'),
    path('carrito/',carrito, name='carrito'),
    path('exito/',exito, name='exito'),
    path('info_producto/<id>',info_producto, name='info_producto'),
    path('pago/',pago, name='pago'),
    path('categoria/',categoria, name='categoria'),
    path('perfil/',perfil, name='perfil'),
    path('perfil/modificar/<id>',modificarPerfil, name='modificar_perfil'),
    path('perfil/modificar_datos/<id>',modificarDatos, name='modificar_datos'),
    #URLS DE LOGIN
    path('login/',login, name='login'),
    path('salir/',salir, name='salir'),
    path('registro/',registro, name='registro'),
    #URLS DE DASHBOARD
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/añadir', añadirProducto, name='añadir'),
    path('dashboard/cliente', listaClientes, name='cliente'),
    path('dashboard/editar/<id>', editarProducto, name='editar'),
    path('dashboard/usuario/<id>', infoUsuario, name='usuario'),
    path('dashboard/productos/', listaProductos, name='productos'),
    path('dashboard/ventas', ventas, name='ventas'),
    path('dashboard/modificar/<id>', modificarCliente, name='modificar'),
    path('dashboard/eliminar/<id>', eliminarCliente, name='eliminar'),
    path('dashboard/eliminarp/<id>', eliminarProducto, name='eliminarp'),
    path('dashboard/modificarp/<id>', modificarProducto, name='modificarp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)