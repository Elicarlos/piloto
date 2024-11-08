from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/dashboard.html')

def sobre(request):
    return render(request, 'sobre.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def contato(request):
    return render(request, 'contato.html')

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

