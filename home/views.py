from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def sobre(request):
    return render(request, 'home/sobre.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def contato(request):
    return render(request, 'home/contato.html')

def perfil(request, nome):
    return render(request, 'home/perfil.html', {"nome": nome})
    
def diasemana(request, dia):
    mensagem = ""
    
    try:
        dia = int(dia)  # Tenta converter dia para inteiro
        if dia > 7 or dia < 1:
            mensagem = "Insira um número de 1 a 7"
        elif dia == 1:
            mensagem = "domingo"
        elif dia == 2:
            mensagem = "segunda-feira"
        elif dia == 3:
            mensagem = "terça-feira"
        elif dia == 4:
            mensagem = "quarta-feira"
        elif dia == 5:
            mensagem = "quinta-feira"
        elif dia == 6:
            mensagem = "sexta-feira"
        elif dia == 7:
            mensagem = "sábado"
    except ValueError:
        mensagem = "Insira um número válido de 1 a 7"  # Mensagem de erro para valores não inteiros

    context = {
        "mensagem": mensagem
    }
    
    return render(request, 'home/dia-semana.html', context)
    
def exibir_item(request, id):
    return render(request, 'home/exibir_item.html', {"id": id})

def lista_produtos(request):
    context = {
        'produtos': [
            {'id': 1, 'nome': 'Camisa Polo', 'preco': 250.00},
            {'id': 2, 'nome': 'Calça Jeans', 'preco': 180.00},
            {'id': 3, 'nome': 'Tênis Esportivo', 'preco': 320.00},
            {'id': 4, 'nome': 'Jaqueta de Couro', 'preco': 450.00},
            {'id': 5, 'nome': 'Relógio Digital', 'preco': 120.00},
            {'id': 6, 'nome': 'Óculos de Sol', 'preco': 200.00},
            {'id': 7, 'nome': 'Boné', 'preco': 80.00},
            {'id': 8, 'nome': 'Mochila', 'preco': 150.00},
            {'id': 9, 'nome': 'Cinto de Couro', 'preco': 90.00},
            {'id': 10, 'nome': 'Carteira de Couro', 'preco': 110.00}
        ],
    }

    return render(request, 'produtos/lista-produtos.html', context)

