from django.db import models
from django.contrib.auth.models import User


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=1)
    isbn = models.IntegerField(max_length=20)
    ano_publicação = models.CharField(max_length=200)


class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_retirada = models.DateField(null=True, blank=True)
    data_devolucao = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username} reservou {self.livro.titulo}"