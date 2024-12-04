from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Doce(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
class Pedido(models.Model):
    numero = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)

class DocesPedido(models.Model):
    quantidade = models.IntegerField()
    produto = models.ForeignKey(Doce, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.produto)