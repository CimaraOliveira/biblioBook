from django.shortcuts import render,redirect
from .models import Livro
from django.contrib import messages
from django.core.paginator import Paginator



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
    messages.success(request,"Livro adicionado com Sucesso!")
    return redirect('listar_livros')

def listar_livros(request):
    livro = Livro.objects.all()
    paginator = Paginator(livro, 6)
    page = request.GET.get('p')
    livro = paginator.get_page(page)
    context = {
        'livro': livro
    }
    return render(request, "core/listar_livros.html", context)


