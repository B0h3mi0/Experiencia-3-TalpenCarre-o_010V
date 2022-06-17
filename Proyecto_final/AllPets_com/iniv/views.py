
from dataclasses import dataclass
from email import message
from pyexpat.errors import messages
from typing_extensions import Self
from django.shortcuts import get_object_or_404, redirect, render

from iniv.forms import ProductoForm,CustomUserCreationForm,ClienteForm
from iniv.models import Producto,Cliente
from django.contrib.auth import authenticate,login,logout
from fastapi import FastAPI

# Create your views here.
def home (request):
    return render(request,'home.html') 
def feriados (request):
    return render(request,'feriados.html') 
def contacto (request):
    return render(request,'contacto.html') 
def somos (request):
    return render(request,'somos.html') 
def galeria (request):
    return render(request,'galery.html') 
def registro (request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method=='POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username= formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login=(request,user)
            messages.success(request,"te has registrado correctamente")
            return redirect(to="home.html")
        data["form"]= formulario
    return render(request,'registro.html',data) 
#############CRUD PRODUCTOS###################
def mostrar(request):
    Productos = Producto.objects.all()
    datos = {
        'productos' : Productos
    }
    return render(request, 'mostrar.html', datos)

def crear_producto(request): 
    if request.method=='POST':
        pro_form= ProductoForm(request.POST, request.FILES)
        if pro_form.is_valid():
            pro_form.save()
            return redirect ('home')
    else:
        pro_form = ProductoForm()
    return render(request, 'crear_producto.html', {'pro_form': pro_form})

def mod_pro(request, id):
    producto = get_object_or_404(Producto,codigo=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = Producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
        
    return render(request, 'mod_producto.html', datos)

def del_pro(request,id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('mostrar')
    return render(request,'registro.html',data) 
#############CRUD PRODUCTOS###################

app = FastAPI()

@app.get("/get-iris")
def get_iris():
    import pandas as pd
    url = 'https://apis.digital.gob.cl/fl/feriados?limit=5'
    iris = pd.read_cvs(url)

    return iris

def logout_request(request):
    logout(request)
    messages.info(request,"Has cerrado sesión")
    return redirect("home")

#############CRUD CLIENTES###################
def mostrar_cli(request):
    Clientes = Cliente.objects.all()
    datos = {
        'clientes' : Clientes
    }
    return render(request, 'mostrar_cli.html', datos)

def crear_cli(request): 
    if request.method=='POST':
        cli_form= ClienteForm(request.POST)
        if cli_form.is_valid():
            cli_form.save()
            return redirect ('home')
    else:
        cli_form = ClienteForm()
    return render(request, 'crear_cli.html', {'cli_form': cli_form})

def modificar_cli(request, id):
    cliente = get_object_or_404(Cliente,rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar_cli')
        
    return render(request, 'modificar_cli.html', datos)

def delete_cli(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar_cli')
#############CRUD CLIENTES###################