from django.shortcuts import render,redirect
from .models import Livro, Reserva
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

def reservar_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    if livro.quantidade > 0:
        Reserva.objects.create(usuario=request.user, livro=livro)
        livro.quantidade -= 1
        livro.save()
        messages.success(request, "Livro Reservado com Sucesso!")
    return redirect('listar_livros')


def minhas_reservas(request):
    reserva = Reserva.objects.filter(usuario=request.user.id)
    paginator = Paginator(reserva, 6)
    page = request.GET.get('p')
    reserva = paginator.get_page(page)
    context = {
        'reserva': reserva
    }
    return render(request, "core/minhas_reservas.html", context)


