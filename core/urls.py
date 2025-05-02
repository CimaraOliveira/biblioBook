from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),
    path('reservar_livro/<int:livro_id>/', views.reservar_livro, name='reservar_livro'),
    path('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('cancelar/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('emprestar/<int:livro_id>/', views.emprestar_livro, name='emprestar_livro'),
    path('devolver/<int:emprestimo_id>/', views.devolver_livro, name='devolver_livro'),
    path('renovar/<int:emprestimo_id>/', views.renovar_emprestimo, name='renovar_emprestimo'),
    path('meus-emprestimos/', views.meus_emprestimos, name='meus_emprestimos'),

]
