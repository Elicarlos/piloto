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


