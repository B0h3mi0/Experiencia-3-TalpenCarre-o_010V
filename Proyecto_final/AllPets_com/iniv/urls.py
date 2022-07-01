from operator import mod
from django.urls import path 
from .views import home, mostrar_cli, registro, somos, feriados,galeria, registro,contacto, mostrar, crear_producto, mod_producto, del_pro, mostrar_cli,crear_cli,modificar_cli,delete_cli
    

urlpatterns =[
    path('',home,name="home"),
    path('somos/', somos, name="somos"),
    path('feriados/',feriados, name="feriados"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name="contacto"),

    
    #############CRUD PRODUCTOS###################
    path('mostrar/', mostrar, name="mostrar"),
    path('crear_producto/',crear_producto, name="crear_producto"),
    path('mod_producto/<id>', mod_producto, name="mod_producto"),
    path('del_pro/<id>', del_pro, name="del_pro"),
    #############CRUD PRODUCTOS###################
    #path('logout/', views.logout_request, name='logout'),


    #############CRUD clientes###################
    path('mostrar_cli/', mostrar_cli, name="mostrar_cli"),
    path('crear_cli/',crear_cli, name="crear_cli"),
    path('modificar_cli/<id>', modificar_cli, name="modificar_cli"),
    path('delete_cli/<id>', delete_cli, name="delete_cli"),
    #############CRUD clientes###################
]