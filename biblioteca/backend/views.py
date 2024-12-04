from urllib import response
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 

class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer 


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer 

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimoSerializer 
    
    @action(detail=True, methods=['get'])
    def emprestimos_cliente(self, request):
        cliente = request.query_params.get('cliente_id')
        emprestimos = Emprestimos.objects.filter(cliente=cliente)
        serializer = EmprestimoSerializer(emprestimos, many=True)
        return response(serializer.data)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer 
    

   