from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Produtos
from .forms import ProdutoForm

# Create your views here.

def base (request):
    return render(request, 'index.html')

#CRUD PRODUTOS:
def listar_Produto(request):
    data = {}
    data['produto'] = Produtos.objects.all()
    return render (request, 'crud.html', data)

def criar_Produto(request):
    data = {}
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_produtos')
    data['form'] = form
    return render(request, 'criar_produto.html', data)

def update_Produto(request, pk):
    data = {}
    produto = Produtos.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('url_listar_produtos')
    data['form'] = form
    return render(request, 'criar_produto.html', data)

def delete_Produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    produto.delete()
    return redirect('url_listar_produtos')

def listar(request):
	data = {}
	data['produto'] = Produtos.objects.all()
	return render (request, 'listar.html', data)

def consulta(request):
    return render(request, 'consulta.html')

def busca(request):
    buscar = request.GET.get('busca')
    resultados = Produtos.objects.filter(nome_produto__icontains=buscar)
    return render(request, 'busca.html', {'resultados':resultados})

def sobre(request):
    return render(request, 'sobre.html')