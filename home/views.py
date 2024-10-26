from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('A view index funcionou, wow!')

def sobre(request):
    return HttpResponse('<h1>Sistema 1.0 desenvolvido por mim mesmo</h1>')


def ajuda(request):
    return HttpResponse('Esta é a pagina de ajuda')


def contato(request):
    return HttpResponse('Esta é a página de contato')


