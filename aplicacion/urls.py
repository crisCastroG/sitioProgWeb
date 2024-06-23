from django.urls import path, include

from .views import busqueda, carrito, dashboard, exito, index, info_producto, login, pago, productos, registro

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
]
