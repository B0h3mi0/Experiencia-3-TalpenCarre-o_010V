from rest_framework import serializers
from iniv.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=['rut','nombre','apellido','correo','direccion','nroTelefono']
        