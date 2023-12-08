from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from django import forms
from django.db import transaction
import datetime
import json

from .models import Admin
from .models import Cliente
from .models import Mecanico
from .models import Pecas
from .models import Veiculo
from .models import Equipe
from .models import OrdemServico
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
    if request.method == "GET": 
        return render(request, 'home.html')

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

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listaClientes.html', {'clientes': clientes})

def addclientes(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')

        cliente = Cliente(nome=nome, email=email, cpf=cpf, telefone=telefone, endereco=endereco)
        cliente.save()

        return redirect('clientes')

    return render(request, 'addCliente.html')

def mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'listaMecanicos.html', {'mecanicos': mecanicos})

def addmecanicos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        especialidade = request.POST.get('especialidade')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        mecanico = Mecanico(nome=nome, cpf=cpf, especialidade=especialidade, endereco=endereco, email=email, telefone=telefone)
        mecanico.save()

        return redirect('mecanicos')

    return render(request, 'addMecanico.html')

def veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'listaVeiculos.html', {'veiculos': veiculos})

def addveiculos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        marca = request.POST.get('marca')
        cor = request.POST.get('cor')
        placa = request.POST.get('placa')
        modelo = request.POST.get('modelo')

        veiculo = Veiculo(nome=nome, marca=marca, cor=cor, placa=placa, modelo=modelo)
        veiculo.save()

        return redirect('veiculos') 

    return render(request, 'addVeiculo.html')

def equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'listaEquipes.html', {'equipes': equipes})

def addequipes(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        especialidade = request.POST['especialidade']
        mecanicos_ids = [int(id) for id in request.POST.getlist('mecanicos') if id]

        equipe = Equipe(nome=nome, descricao=descricao, especialidade=especialidade)
        equipe.save()
        equipe.mecanicos.set(mecanicos_ids)  # Adicionar mecânicos à equipe

        return redirect('equipes')

    mecanicos = Mecanico.objects.all()
    return render(request, 'addEquipe.html', {'mecanicos': mecanicos})

def addordemservico(request):
    equipes = Equipe.objects.all()
    pecas = Pecas.objects.all()

    if request.method == 'POST':
        try:
            # Obter dados do formulário
            placa = request.POST.get('placa')
            nome_cliente = request.POST.get('nome_cliente')
            modelo_carro = request.POST.get('modelo_carro')
            cor_carro = request.POST.get('cor_carro')
            problema = request.POST.get('problema')
            data_entrada = request.POST.get('data_entrada')
            data_prevista = request.POST.get('data_prevista')
            equipe_id = request.POST.get('equipe')
            preco_total = request.POST.get('preco_total')
            pecas_data = request.POST.get('pecas_json')
            pecas_data = json.loads(pecas_data)
            mecanicos_ids = request.POST.getlist('mecanicos')

            # Convertendo strings para os tipos de dados apropriados
            data_entrada = timezone.datetime.strptime(data_entrada, "%Y-%m-%dT%H:%M")
            data_prevista = timezone.datetime.strptime(data_prevista, "%Y-%m-%dT%H:%M")

            # Criar o cliente (ou obter se já existir com o mesmo nome)
            cliente, created = Cliente.objects.get_or_create(
                nome=nome_cliente,
                defaults={'email': 'default@email.com', 'telefone': '123456789', 'cpf': '12345678901', 'endereco': 'Endereço padrão'}
            )

            # Tratar o preço total
            preco_total = float(preco_total) if preco_total and preco_total != '' else 0.0

            # Criar o veículo associado ao cliente (ou obter se já existir com a mesma placa)
            veiculo, created = Veiculo.objects.get_or_create(
                placa=placa,
                defaults={'cliente': cliente, 'modelo': modelo_carro, 'cor': cor_carro}
            )

            # Obter a equipe selecionada
            equipe = Equipe.objects.get(id=equipe_id)

            # Obter a lista de peças selecionadas
            pecas_ids = [item['id'] for item in pecas_data]
            pecas_selecionadas = Pecas.objects.filter(id__in=[int(item) for item in pecas_ids])

            # Usar uma transação para garantir que as operações no banco de dados sejam atômicas
            with transaction.atomic():
                # Criar a ordem de serviço
                ordem_servico = OrdemServico(
                    dataEmissao=timezone.now(),
                    dataConclusao=data_prevista,
                    valor=preco_total,
                    descricao=problema,
                    status='pendente',
                    veiculo=veiculo,
                )
                
                ordem_servico.cliente = cliente
                ordem_servico.equipe = equipe 

                ordem_servico.save()

                # Criar as relações entre peças e ordem de serviço usando o modelo PecasOrdemServico
                for peca in pecas_selecionadas:
                    PecasOrdemServico.objects.create(pecas=peca, ordem_servico=ordem_servico)

            print("Ordem de Serviço criada com sucesso:", ordem_servico.id)
            return redirect('listaordensservico')

        except Equipe.DoesNotExist:
            raise Http404("A equipe especificada não existe.")
        except Pecas.DoesNotExist:
            raise Http404("Uma ou mais peças especificadas não existem.")

    return render(request, 'addOrdemServico.html', {'equipes': equipes, 'pecas': pecas})

def listaordensservico(request):
    ordens_servico = OrdemServico.objects.all()
    return render(request, 'listaOrdensServico.html', {'ordens_servico': ordens_servico})

def logout(request):
    return redirect('login')
