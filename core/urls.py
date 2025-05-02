from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),
    path('reservar_livro/<int:livro_id>/', views.reservar_livro, name='reservar_livro'),
    path('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('cancelar/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),

]
