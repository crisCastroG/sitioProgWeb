from django.shortcuts import render
from .models import CarroCompra, Cliente, Producto, ProductoCarro
from django.shortcuts import get_object_or_404, redirect
from .forms import UpdClienteForm, ProductoForm, UpdProductoForm, CustomCreationForm, UpdVentaForm
from django.contrib import messages
from os import path, remove
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

# Views del sitio
def index(request):
    productos = Producto.objects.all()
    datos = {
        "productos" : productos
    }
    return render(request,'aplicacion/index.html',datos)

def busqueda(request):
    return render(request,'aplicacion/busqueda.html')

def perfil(request):
    cliente, clienteCreado = Cliente.objects.get_or_create(email = request.user.email)

    datos = {
        'cliente' : cliente
    }

    return render(request,'aplicacion/perfil_usuario.html', datos)

def modificarPerfil(request, id):
    cliente = get_object_or_404(Cliente, email = id)
    form = UpdClienteForm(instance = cliente)

    if request.method == "POST":
        form = UpdClienteForm(request.POST, files = request.FILES, instance = cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente modificado")
            return redirect(to="perfil")

    datos = {
        'cliente' : cliente,
        'form' : form
    }

    return render(request,'aplicacion/modificar_perfil.html', datos)

def modificarDatos(request, id):
    cliente = get_object_or_404(Cliente, email = id)
    form = UpdClienteForm(instance = cliente)

    if request.method == "POST":
        form = UpdClienteForm(request.POST, files = request.FILES, instance = cliente)
        if form.is_valid():
            form.save()
            return redirect(to="pago")

    datos = {
        'cliente' : cliente,
        'form' : form
    }

    return render(request,'aplicacion/modificar_datos.html', datos)

def carrito(request):
    carroCompra = CarroCompra.objects.filter(email_id = request.user.email)
    total = 0
    for producto in carroCompra:
        total += producto.cantidad * int(Producto.objects.get(codigo = producto.producto_id).precio)
    datos = {
        'carrito' : carroCompra,
        'total' : total
    }
    return render(request,'aplicacion/carrito.html', datos)

def exito(request):
    return render(request,'aplicacion/exito.html')

def info_producto(request, id):
    producto = get_object_or_404(Producto, codigo = id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad'))
        carroCompra, creado = CarroCompra.objects.get_or_create(email_id = request.user.email, producto_id = id)
        if creado == True:
            CarroCompra.objects.filter(producto_id = id, email_id = request.user.email).update(cantidad = cantidad)
        else:
            cantidadActual = CarroCompra.objects.get(email_id = request.user.email, producto_id = id).cantidad
            CarroCompra.objects.filter(producto_id = id, email_id = request.user.email).update(cantidad = cantidadActual + cantidad) 
        messages.success(request, "Producto agregado al carro")
        redirect(to='aplicacion/info_producto.html') 
    datos = {
        "producto" : producto
    }

    return render(request,'aplicacion/info_producto.html', datos)

def login(request):
    return render(request,'aplicacion/registration/login.html')

def salir(request):
    logout(request)
    return redirect(to='index')

def pago(request):
    carroCompra = CarroCompra.objects.filter(email_id = request.user.email)
    cliente, clienteCreado = Cliente.objects.get_or_create(email = request.user.email)
    total = 0
    form = UpdClienteForm(instance = cliente)
    for producto in carroCompra:
        total += producto.cantidad * int(Producto.objects.get(codigo = producto.producto_id).precio)
    datos = {
        'carrito' : carroCompra,
        'total' : total,
        'cliente' : cliente,
        'form' : form
    }
    return render(request,'aplicacion/pago.html', datos)

def productos(request):
    return render(request,'aplicacion/productos.html')

def registro(request):
    data = {
        'form': CustomCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomCreationForm(data = request.POST)
        if request.method=="POST":
                form=CustomCreationForm(data = request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Registro de usuario exitoso")
                    return redirect(to="index")                    
        data["form"] = formulario
    return render(request,'registration/registro.html', data)

# Sitios del dashboard
@staff_member_required
def dashboard(request):
    return render(request,'aplicacion/dashboard/dashboard.html')
@staff_member_required
def añadirProducto(request):
    return render(request,'aplicacion/dashboard/añadirproducto.html')
@staff_member_required
#def listaClientes(request):
    #return render(request,'aplicacion/dashboard/listaclientes.html')
@staff_member_required
def editarProducto(request):
    return render(request,'aplicacion/dashboard/editarproducto.html')
@staff_member_required
def infoUsuario(request):
    return render(request,'aplicacion/dashboard/infousuario.html')
@staff_member_required
def listaProductos(request):
    return render(request,'aplicacion/dashboard/listaproductos.html')
@staff_member_required
def ventas(request):
    return render(request,'aplicacion/dashboard/ventas.html')
@staff_member_required
def modificarCliente(request):
    return render(request,'aplicacion/dashboard/modificarcliente.html')
@staff_member_required
def eliminarCliente(request):
    return render(request,'aplicacion/dashboard/eliminarcliente.html')
@staff_member_required
def eliminarProducto(request):
    return render(request,'aplicacion/dashboard/eliminarproducto.html')
@staff_member_required
def modificarProducto(request):
    return render(request,'aplicacion/dashboard/modificarproducto.html')
def detalleVenta(request):
    return render(request,'aplicacion/dashboard/detalles_venta.html')

@staff_member_required
def listaClientes(request):
    clientes=Cliente.objects.all()
    
    datos={
        "clientes":clientes
    }

    return render(request,'aplicacion/dashboard/listaclientes.html', datos)

@staff_member_required
def infoUsuario(request, id):
    
    #persona=Persona.objects.get(rut=id)
    cliente=get_object_or_404(Cliente,rut=id)
    
    datos={
        "cliente":cliente
    }
    return render(request,'aplicacion/dashboard/infousuario.html',datos)

@staff_member_required
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

@staff_member_required
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

@staff_member_required
def listaProductos(request):
    productos=Producto.objects.all()
    
    datos={
        "productos":productos
    }

    return render(request,'aplicacion/dashboard/listaproductos.html', datos)

@staff_member_required
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

@staff_member_required
def editarProducto(request, id):
    
    producto=get_object_or_404(Producto,codigo=id)
    
    datos={
        "producto":producto
    }
    return render(request,'aplicacion/dashboard/editarproducto.html',datos)

@staff_member_required
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

@staff_member_required
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

def ventas(request):
    pedido=Pedidos.objects.all()
    clientes=Cliente.objects.all()
    

    datos={
        "pedido":pedido,
        "clientes":clientes
    }

    return render(request,'aplicacion/dashboard/ventas.html', datos)

def detalleVenta(request,id):
    pedidos=get_object_or_404(Pedidos, nro_pedido=id)
    cliente=get_object_or_404(Cliente, )
    form=UpdVentaForm(instance=pedidos)
    
    
    if request.method=="POST":
         form=UpdVentaForm(request.POST, files=request.FILES, instance=pedidos)
         if form.is_valid():
             form.save()
             messages.set_level(request,messages.WARNING)
             messages.warning(request,"Venta modificada")
             return redirect(to="ventas")
    
    datos={
        'pedidos':pedidos,
        'form':form
    }
    return render(request,'aplicacion/dashboard/detalles_venta.html',datos)
