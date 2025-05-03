from django.shortcuts import render,redirect, get_object_or_404
from .models import Livro, Reserva, Emprestimo
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone


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
    livro = get_object_or_404(Livro, id=livro_id)
    #Conta reservas ativas do usuário
    reservas_ativas = Reserva.objects.filter(usuario=request.user, ativo=True).count()

    if reservas_ativas >= 3:
        messages.error(request, "Você já reservou 3 livros. Cancele uma reserva para fazer uma nova.")
    elif not livro.disponivel:
        messages.warning(request, "Este livro não está disponível no momento.")
    else:
        Reserva.objects.create(usuario=request.user, livro=livro)
        livro.disponivel = False
        livro.save()
        messages.success(request, "Livro reservado com sucesso!")
    return redirect('listar_livros')


def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id, usuario=request.user)

    if reserva.ativo:
        reserva.ativo = False
        reserva.save()

        livro = reserva.livro
        livro.disponivel = True
        livro.save()

        messages.success(request, "Reserva cancelada com sucesso.")
    else:
        messages.error(request, "Esta reserva já foi cancelada.")

    return redirect('minhas_reservas')



def minhas_reservas(request):
    reserva = Reserva.objects.filter(usuario=request.user.id, ativo=True)
    reservas_canceladas = Reserva.objects.filter(usuario=request.user, ativo=False)
    paginator = Paginator(reserva, 6)
    page = request.GET.get('p')
    reserva = paginator.get_page(page)

    return render(request, "core/minhas_reservas.html",
                  {
                      'reserva': reserva,
                      'reservas_canceladas': reservas_canceladas,
                  })


def emprestar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if livro.disponivel:
        Emprestimo.objects.create(usuario=request.user, livro=livro)
        livro.disponivel = False
        livro.save()
        messages.success(request, "Livro emprestado com sucesso!")
    else:
        messages.error(request, "Este livro não está disponível para empréstimo!")
    return redirect('listar_livros')

def devolver_livro(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id, usuario=request.user)
    if not emprestimo.data_devolucao:
        emprestimo.data_devolucao = timezone.now()
        emprestimo.save()

        livro = emprestimo.livro
        livro.disponivel = True
        livro.save()

        messages.success(request, "Livro devolvido com sucesso.")
    else:
        messages.error(request, "Este livro já foi devolvido.")
    return redirect('meus_emprestimos')

def renovar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id, usuario=request.user)
    if not emprestimo.renovado and not emprestimo.data_devolucao:
        emprestimo.data_emprestimo = timezone.now()
        emprestimo.renovado = True
        emprestimo.save()
        messages.success(request, "Empréstimo renovado por mais 7 dias.")
    else:
        messages.error(request, "Não é possível renovar este empréstimo.")
    return redirect('meus_emprestimos')


def meus_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-data_emprestimo')
    emprestimos_ativos = Emprestimo.objects.filter(usuario=request.user, data_devolucao__isnull=True).order_by('-data_emprestimo')
    emprestimos_concluidos = Emprestimo.objects.filter(usuario=request.user, data_devolucao__isnull=False).order_by('-data_devolucao')

    return render(request, 'core/meus_emprestimos.html', {
        'emprestimos_ativos': emprestimos_ativos,
        'emprestimos_concluidos': emprestimos_concluidos,
        'emprestimos': emprestimos,
    })

