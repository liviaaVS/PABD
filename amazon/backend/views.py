from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = EnderecoSerializer

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset =  FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset =  Item.objects.all()
    serializer_class = ItemSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset =  Pedido.objects.all()
    serializer_class = PedidoSerializer


def index(request):
    # Faça a requisição para sua API (substitua a URL pelo endpoint correto)
    url = "http://itens/"
    
    # Consuma a API
    response = requests.get(url)
    
    # Verifique se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()  # Converte a resposta para JSON
    else:
        data = []  # Caso a API não retorne dados válidos, podemos retornar uma lista vazia

    # Passe os dados para o contexto
    context = {
        'produtos': data
    }
    
    return render(request, "index.html")