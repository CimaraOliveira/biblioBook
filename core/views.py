from django.shortcuts import render,redirect
from .models import Livro

def index(request):
    return render(request, 'core/index.html')

def cadastro_livro(request):
    if request.method != 'POST':
        return render(request, 'core/cadastro_livro.html')

    titulo = request.POST['titulo']
    autor = request.POST['autor']
    quantidade = request.POST['quantidade']
    isbn = request.POST['isbn']
    ano_publicação = request.POST['ano_publicação']

    cadastrarLivro = Livro(titulo=titulo, autor=autor,  quantidade= quantidade, isbn=isbn,
                                                ano_publicação=ano_publicação)
    cadastrarLivro.save()
    return redirect('cadastro_livro/')

 
