from django.shortcuts import render
from .models import Cliente
from django.shortcuts import get_object_or_404, redirect
from .forms import UpdClienteForm
from django.contrib import messages
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
#def listaClientes(request):
    #return render(request,'aplicacion/dashboard/listaclientes.html')
def editarProducto(request):
    return render(request,'aplicacion/dashboard/editarproducto.html')
def infoUsuario(request):
    return render(request,'aplicacion/dashboard/infousuario.html')
def listaProductos(request):
    return render(request,'aplicacion/dashboard/listaproductos.html')
def ventas(request):
    return render(request,'aplicacion/dashboard/ventas.html')
def modificarCliente(request):
    return render(request,'aplicacion/dashboard/modificarcliente.html')
def eliminarCliente(request):
    return render(request,'aplicacion/dashboard/eliminarcliente.html')

def listaClientes(request):
    clientes=Cliente.objects.all()
    
    datos={
        "clientes":clientes
    }

    return render(request,'aplicacion/dashboard/listaclientes.html', datos)

def infoUsuario(request, id):
    
    #persona=Persona.objects.get(rut=id)
    cliente=get_object_or_404(Cliente,rut=id)
    
    datos={
        "cliente":cliente
    }
    return render(request,'aplicacion/dashboard/infousuario.html',datos)

def modificarCliente(request,id):
    cliente=get_object_or_404(Cliente, rut=id)
    form=UpdClienteForm(instance=cliente)
    
    
    if request.method=="POST":
         form=UpdClienteForm(request.POST, files=request.FILES, instance=cliente)
         if form.is_valid():
             form.save()
             messages.set_level(request,messages.WARNING)
             messages.warning(request,"Cliente modificado")
             return redirect(to="cliente")
    
    datos={
        'cliente':cliente,
        'form':form
    }
    return render(request,'aplicacion/dashboard/modificarcliente.html',datos)