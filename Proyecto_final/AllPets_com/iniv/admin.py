from django.contrib import admin
from .models import Categoria, Producto,Cliente,Stock,Compra,DetalleCompra

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Stock)
admin.site.register(Compra)
admin.site.register(DetalleCompra)