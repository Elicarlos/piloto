from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def contato(request):
    return render(request, 'contato.html')

def perfil(request, nome):
    return render(request, 'perfil.html', {"nome": nome})
    
def diasemana(request, dia):
    
    try:
        dia = int(dia)
    
    except ValueError:
        return HttpResponseBadRequest("Insira um valor numérico para o dia.")
    
  
    mensagem = ""
    
    if dia > 7 :
        mensagem ="Digite um numero menor que 7"
        
    elif dia == 0:
        mensagem = "Insira um numero de 1  a 7"
        
    if dia == 1:
        mensagem = "domingo"
    
    if dia ==2:
        mensagem = "segunda-feira"
        
    if dia == 3:
        mensagem = "terça-feira"
        
    if dia == 4:
        mensagem = "quarta-feira"
        
    if dia == 5:
        mensagem = "quinta-feira"
        
    if dia == 6:
        mensagem = "sexta-feira"
        
    if dia == 7:
        mensagem = "sexta-feira"
        
   
    
    
    context = {
        "mensagem": mensagem
    }
    
    return render(request, 'dia-semana.html', context)


def exibir_item(request, id):
    return render(request, 'exibir_item.html', {"id": id})


def dashboard(request):
    return render(request, 'home/dashboard.html')


