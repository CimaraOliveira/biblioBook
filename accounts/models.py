from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    slug = models.SlugField('Atalho', max_length=200, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)