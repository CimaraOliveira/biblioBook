from django.contrib import admin
from .models import Livro, Reserva, Emprestimo

class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'isbn']

admin.site.register(Livro)
admin.site.register(Reserva)
admin.site.register(Emprestimo)
