from string import digits
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.nome

class Endereco (models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone =  models.CharField(max_length=20)



class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=255)

class Item (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return f'{self.nome} - {self.descricao} - R$ {self.preco} - Estoque: {self.estoque}'


class Pedido(models.Model):
    PENDENTE = 'Pendente'
    EM_ANDAMENTO = 'Em andamento'
    CONCLUÍDO = 'Concluído'
    CANCELADO = 'Cancelado'
    
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (EM_ANDAMENTO, 'Em andamento'),
        (CONCLUÍDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDENTE)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente} - {self.status} - {self.data_pedido.strftime("%d/%m/%Y %H:%M")}'