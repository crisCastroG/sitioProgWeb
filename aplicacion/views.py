from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'aplicacion/index.html')

def busqueda(request):
    return render(request,'aplicacion/busqueda.html')

def carrito(request):
    return render(request,'aplicacion/carrito.html')

def exito(request):
    return render(request,'aplicacion/exito.html')

def info_producto(request):
    return render(request,'aplicacion/info_producto.html')

def login(request):
    return render(request,'aplicacion/login.html')

def pago(request):
    return render(request,'aplicacion/pago.html')

def productos(request):
    return render(request,'aplicacion/productos.html')

def registro(request):
    return render(request,'aplicacion/registro.html')

# Sitios del dashboard
def dashboard(request):
    return render(request,'aplicacion/dashboard/dashboard.html')
def añadirProducto(request):
    return render(request,'aplicacion/dashboard/añadirproducto.html')
def listaClientes(request):
    return render(request,'aplicacion/dashboard/listaclientes.html')
def editarProducto(request):
    return render(request,'aplicacion/dashboard/editarproducto.html')
def infoUsuario(request):
    return render(request,'aplicacion/dashboard/infousuario.html')
def listaProductos(request):
    return render(request,'aplicacion/dashboard/listaproductos.html')
def ventas(request):
    return render(request,'aplicacion/dashboard/ventas.html')
