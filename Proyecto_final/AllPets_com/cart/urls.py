from operator import mod
from django.urls import path 
 
from .import views   

app_name='carrito'

urlpatterns =[
    
    
    path('agregar/<codigo>', views.agregar_producto,name='agregar'),
    path('eliminar/<codigo>', views.eliminar_producto, name='eliminar'),
    path('restar/<codigo>', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
]