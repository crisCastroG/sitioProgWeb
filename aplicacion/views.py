from django.shortcuts import render
from .models import Cliente, Producto
from django.shortcuts import get_object_or_404, redirect
from .forms import UpdClienteForm, ProductoForm, UpdProductoForm
from django.contrib import messages
from os import path, remove
from django.conf import settings
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
def eliminarProducto(request):
    return render(request,'aplicacion/dashboard/eliminarproducto.html')
def modificarProducto(request):
    return render(request,'aplicacion/dashboard/modificarproducto.html')

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

def eliminarCliente(request, id):
    cliente=get_object_or_404(Cliente,rut=id)

    datos={
        "cliente":cliente
    }

    if request.method=="POST":
        if cliente.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+cliente.imagen.url))
        cliente.delete()
        messages.error(request, 'Cliente Eliminado')
        return redirect(to='cliente')
 
        
    return render(request,'aplicacion/dashboard/eliminarcliente.html',datos)

#### PRODUCTOS ####

def listaProductos(request):
    productos=Producto.objects.all()
    
    datos={
        "productos":productos
    }

    return render(request,'aplicacion/dashboard/listaproductos.html', datos)

def añadirProducto(request):
    
    form=ProductoForm()

    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado al registro')
            return redirect(to="productos")

    datos={
        "form":form
    }
    return render(request,'aplicacion/dashboard/añadirproducto.html', datos)

def editarProducto(request, id):
    
    producto=get_object_or_404(Producto,codigo=id)
    
    datos={
        "producto":producto
    }
    return render(request,'aplicacion/dashboard/editarproducto.html',datos)

def modificarProducto(request,id):
    producto=get_object_or_404(Producto, codigo=id)
    form=UpdProductoForm(instance=producto)
    
    
    if request.method=="POST":
         form=UpdProductoForm(request.POST, files=request.FILES, instance=producto)
         if form.is_valid():
             form.save()
             messages.set_level(request,messages.WARNING)
             messages.warning(request,"Producto modificado")
             return redirect(to="productos")
    
    datos={
        'producto':producto,
        'form':form
    }
    return render(request,'aplicacion/dashboard/modificarproducto.html',datos)

def eliminarProducto(request, id):
    producto=get_object_or_404(Producto,codigo=id)

    datos={
        "producto":producto
    }

    if request.method=="POST":
        if producto.foto_pro:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+producto.foto_pro.url))
        producto.delete()
        messages.error(request, 'Producto Eliminado')
        return redirect(to='productos')
    return render(request,'aplicacion/dashboard/eliminarproducto.html',datos)
