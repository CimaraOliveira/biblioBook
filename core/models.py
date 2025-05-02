from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editora = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    isbn = models.IntegerField(max_length=20)
    disponivel = models.BooleanField(default=True)
    ano_publicação = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField('Data Reserva', default=timezone.now)
    data_retirada = models.DateField(null=True, blank=True)
    data_devolucao = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(verbose_name='Status', default=True)

    def __str__(self):
        return f"{self.usuario.username} reservou {self.livro.titulo}"

    def status_display(self):
        return "✅ Ativa" if self.ativo else "❌ Cancelada"

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    renovado = models.BooleanField(default=False)

    @property
    def esta_atrasado(self):
        prazo = self.data_emprestimo + timedelta(days=7)
        return timezone.now() > prazo and not self.data_devolucao

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo}"