from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),

]
