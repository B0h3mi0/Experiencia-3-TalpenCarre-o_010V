from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Cliente, Producto
from django.contrib.auth.forms import UserCreationForm


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo', 'nombre', 'marca','precio','categoria','imagen']
        labels ={
            'codigo':'Codigo' ,
            'nombre':'Nombre',
            'marca':'Marca',
            'precio':'Precio',
            'categoria':'Categoria',
            'imagen':'Imagen'
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese codigo', 
                    'id': 'codigo'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese imagen', 
                    'id': 'imagen',
                }
            ),

        }

class CustomUserCreationForm(UserCreationForm):

    pass


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'apellido','edad','sexo','nroTelefono']
        labels ={
            'rut':'Rut' ,
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'sexo':'Sexo',
            'nroTelefono':'Numero de Telefono'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellido', 
                    'id': 'apellido'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Edad', 
                    'id': 'edad'
                }
            ),
            'sexo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Sexo', 
                    'id': 'sexo'
                }
            ),
            'nroTelefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Telefono', 
                    'id': 'nroTelefono'
                }
            ),

        }