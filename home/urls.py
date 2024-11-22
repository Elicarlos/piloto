from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="home"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    path('sobre/', views.sobre, name="sobre"),
    path('perfil/<str:nome>/', views.perfil, name="perfil"),
    path('item/<int:id>/', views.exibir_item, name="item"),
    path('diasemana/<int:dia>/', views.diasemana, name="diasemana"),
    path('produtos/', views.lista_produtos, name="produtos"),
    path('produtos/form/', views.adiciona_produto, name="adiciona_produto"),
    path('detalhes_produto/<int:id>/', views.detalhes_produto, name="detalhes_produto"),
    path('editar_produto/<int:id>/', views.editar_produto, name="editar_produto"),
    path('excluir_produto/<int:id>/', views.excluir_produto, name="excluir_produto")
]



