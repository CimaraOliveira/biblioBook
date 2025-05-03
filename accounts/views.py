from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login as auth_login


def login_view(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        messages.success(request, 'Login efetuado com sucesso!')
        return render(request, 'core/listar_livros.html')

    messages.error(request, 'E-mail e/ou senha inválidos!')
    return redirect('login')



