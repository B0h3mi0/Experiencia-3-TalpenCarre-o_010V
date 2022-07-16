from django.shortcuts import render
from  .carrito import Carrito
from iniv.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request,codigo):

    carrito=Carrito(request)
    producto=Producto.objects.get(id=codigo)
    carrito.agregar(producto=producto)

    return redirect("galery")

def eliminar_producto(request, codigo):

    carrito=Carrito(request)
    producto=Producto.objects.get(id=codigo)
    carrito.eliminar(producto=producto)

    return redirect("galery")

def restar_producto(request, codigo):

    carrito=Carrito(request)
    producto=Producto.objects.get(id=codigo)
    carrito.restar_producto(producto=producto)

    return redirect("galery")

def limpiar_carrito(request):

    carrito=Carrito(request)
    carrito.limpiar_carrito()
    return redirect("galery")
