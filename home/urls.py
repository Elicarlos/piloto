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

]