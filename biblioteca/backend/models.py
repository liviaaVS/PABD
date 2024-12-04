from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"Usuario: {self.nome} (CPF: {self.cpf})"


class Editora(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"Autor: {self.nome}"


class Livro(models.Model):
    nome = models.CharField(max_length=255)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    data_publicacao = models.DateField()
    edicao = models.IntegerField(default=1)

    def __str__(self):
        return f"Livro: {self.nome} (Edição {self.edicao})"


class Emprestimos(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return f"Empréstimo: {self.user.nome} - {self.livro.nome} ({self.data_emprestimo})"


class Reserva(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField()
    data_fim_reserva = models.DateTimeField()

    def __str__(self):
        return f"Reserva: {self.user.nome} - {self.livro.nome} (Até {self.data_fim_reserva})"
