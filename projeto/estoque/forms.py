from dataclasses import field, fields
from django.forms import ModelForm
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['id_produto', 'nome_produto', 'quantidade_produto']