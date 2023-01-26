"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from estoque.views import base, listar_Produto, criar_Produto, update_Produto, delete_Produto, listar, consulta, busca, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='estoque'),

    path('listar_produtos/', listar_Produto, name='url_listar_produtos'),
    path('criar_produto/', criar_Produto, name='url_criar_produto'),
    path('update_produto/<int:pk>/', update_Produto, name='url_update_produto'),
    path('delete_produto/<int:pk>/', delete_Produto, name='url_delete_produto'),
    path('consulta/', consulta, name='url_consulta'),
    path('listar/', listar, name='url_listar'),
    path('busca/', busca, name='url_busca'),
    path('account/', include('django.contrib.auth.urls')),
    path('sobre/', sobre, name='url_sobre'),
]
