from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Admin
from .models import Cliente
from .models import Mecanico
from .models import Pecas
from .models import Veiculo
from .models import OrdemServico
from .models import Equipe
from .models import PecasOrdemServico

def login (request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            admin = Admin.objects.get(email=email)
            if admin.senha == senha:
                return render(request, 'home.html')
            else:
                return render(request, 'login.html', {'erro': 'Senha incorreta'})
        except Admin.DoesNotExist:
            return render(request, 'login.html', {'erro': 'Usuário não encontrado'})

def home (request):
    return HttpResponse("Esta no home!")

def pecas(request):
    pecas = Pecas.objects.all()
    return render(request, 'listaPecas.html', {'pecas': pecas})

def addpecas(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        marca = request.POST.get('marca')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        peca = Pecas(nome=nome, marca=marca, preco=preco, quantidade=quantidade)
        peca.save()

        return redirect('pecas')

    return render(request, 'addPeca.html')