from django.db import models

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
    imagen=models.ImageField(upload_to='images/',null='True',blank='True', verbose_name='Imagen del producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.codigo


######### CLIENTE ########
class Cliente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre= models.CharField(null='True', max_length=20, verbose_name='Nombre')
    apellido=models.CharField(null='True', max_length=20, verbose_name='Apellido')
    correo=models.CharField(null='True', max_length=50,verbose_name='Correo')
    direccion=models.CharField(null='True',max_length=50,verbose_name='Direccion')
    nroTelefono=models.CharField(null='True', max_length=15, verbose_name='Telefono')

    def __str__(self):
        return self.rut
