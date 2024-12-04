from rest_framework import serializers

from .models import *  # Replace with your actual model names

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  

class DoceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doce
        fields = '__all__'  


class DocesPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocesPedido
        fields = '__all__'  

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocesPedido
        fields = '__all__'  