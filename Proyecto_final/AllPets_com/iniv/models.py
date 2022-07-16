from pyexpat import model
from django.db import models
from numpy import character

# Create your models here.


#########  CATEGORIA  ######
class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='ID de Categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')
    def __str__(self):
        return self.nombreCategoria

######### PRODUCTO ########
class Producto(models.Model):
    codigo = models.CharField( max_length=20, primary_key=True, verbose_name='Codigo del  Producto')
    nombre= models.CharField(max_length=20, verbose_name='Nombre del Producto')
    marca=models.CharField(max_length=20, verbose_name='Marca')
    precio=models.IntegerField( verbose_name='Precio')
    imagen=models.ImageField(upload_to='images/',blank='True',null='True', verbose_name='Imagen del producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    def __str__(self):
        return self.codigo

######### CLIENTE ########
class Cliente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut', unique=True)
    nombre= models.CharField(null='True', max_length=20, verbose_name='Nombre')
    apellido=models.CharField(null='True', max_length=20, verbose_name='Apellido')
    correo=models.EmailField(null='True', max_length=50,verbose_name='Correo')
    direccion=models.CharField(null='True',max_length=50,verbose_name='Direccion')
    nroTelefono=models.CharField(null='True', max_length=15, verbose_name='Telefono')
    def __str__(self):
        return self.rut

######### STOCK ########
class Stock(models.Model):
    nombre= models.CharField(max_length=20, verbose_name='Nombre del Producto')
    cantidad= models.IntegerField(verbose_name='Cantidad')
    codigo=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='codigo')
    def __str__(self):
        return self.nombre

######### COMPRA ########
class Compra(models.Model):
    idCompra= models.AutoField(primary_key=True)
    nombreCliente= models.CharField( max_length=20, verbose_name='Nombre cliente')
    apellidoCliente=models.CharField( max_length=20, verbose_name='Apellido cliente')
    direccion=models.CharField(max_length=50,verbose_name='Direccion')
    totalCompra=models.IntegerField(verbose_name='Total de compra')
    estado=models.CharField(verbose_name='Estado de compra', max_length=20)
    rut = models.ForeignKey(Cliente,on_delete=models.CASCADE, verbose_name='Rut cliente')
    def __str__(self):
        return self.idCompra

######### DETALLE COMPRA ########
class DetalleCompra(models.Model):
    rut = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Rut  cliente')
    idCompra= models.ForeignKey(Compra,on_delete=models.CASCADE, verbose_name='id compra')
    codigo=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='codigo')
    cantidad= models.IntegerField(verbose_name='Cantidad')
    totalCompra=models.IntegerField(verbose_name='Total de compra')
    def __str__(self):
        return self.idCompra