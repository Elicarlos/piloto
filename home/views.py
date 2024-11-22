from django.http import HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect
from . forms import ContatoForm, ProdutoForm
from . models import Produto


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def sobre(request):
    return render(request, 'home/sobre.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form
        
    }
    return render(request, 'home/contato.html', contexto)

def perfil(request, nome):
    return render(request, 'home/perfil.html', {"nome": nome})
    
def diasemana(request, dia):
    # Dicionário para mapear os dias da semana
    dias_semana = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado",
    }
    
    # Verifica se o número está no intervalo válido
    if 1 <= dia <= 7:
        mensagem = f"O dia selecionado é {dias_semana[dia]}."
    else:
        mensagem = "Erro: Insira um número entre 1 e 7."
    
    # Define o contexto com a mensagem
    context = {
        "mensagem": mensagem
    }
    
    # Renderiza a página com o contexto
    return render(request, 'home/dia-semana.html', context)

    
def exibir_item(request, id):
    return render(request, 'home/exibir_item.html', {"id": id})

def lista_produtos(request):
    produtos = Produto.objects.all()
    context = {
        # 'produtos': [
        #     {'id': 1, 'nome': 'Camisa Polo', 'preco': 250.00},
        #     {'id': 2, 'nome': 'Calça Jeans', 'preco': 180.00},
        #     {'id': 3, 'nome': 'Tênis Esportivo', 'preco': 320.00},
        #     {'id': 4, 'nome': 'Jaqueta de Couro', 'preco': 450.00},
        #     {'id': 5, 'nome': 'Relógio Digital', 'preco': 120.00},
        #     {'id': 6, 'nome': 'Óculos de Sol', 'preco': 200.00},
        #     {'id': 7, 'nome': 'Boné', 'preco': 80.00},
        #     {'id': 8, 'nome': 'Mochila', 'preco': 150.00},
        #     {'id': 9, 'nome': 'Cinto de Couro', 'preco': 90.00},
        #     {'id': 10, 'nome': 'Carteira de Couro', 'preco': 110.00}
        # ],
        'produtos': produtos 
    }

    return render(request, 'produtos/lista-produtos.html', context)

def adiciona_produto(request):   
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()            
            redirect('produtos')            
    else:
        form = ProdutoForm()
    
    return render(request, 'produtos/produto-form.html', {'form': form})


def detalhes_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)    
    except Produto.DoesNotExist:
        raise Http404('Produto não existe')
    return render(request, 'produtos/detalhe-produto.html', {'produto': produto})

    
def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form  = ProdutoForm(instance=produto)
    
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    context ={
        'form': form
    }
    
    return render(request, 'produtos/editar-produto.html', context)


def excluir_produto(request, id):
    produto = Produto.objects.get(id=id)    
    
    if request.method == "GET":
        produto.delete()
        return redirect('produtos')
    
    # return render(request,'produtos/delete-produto.html', {'produto': produto})