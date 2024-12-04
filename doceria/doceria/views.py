from django.shortcuts import render
from rest_framework import viewsets
from doceria.models import *
from doceria.serializers import *

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DoceViewSet(viewsets.ModelViewSet):
    queryset = Doce.objects.all()
    serializer_class = DoceSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DocesPedidoViewSet(viewsets.ModelViewSet):
    queryset = DocesPedido.objects.all()
    serializer_class = DocesPedidoSerializer

