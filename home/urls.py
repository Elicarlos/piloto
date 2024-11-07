from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    path('sobre/', views.sobre, name="sobre"),
    path('perfil/<str:nome>/', views.perfil, name="perfil"),
    path('item/<int:id>/', views.exibir_item, name="exibir_item"),
    path('diasemana/<int:dia>/', views.diasemana, name="diasemana"),
    path('dashboard/', views.dashboard, name="dashboard"),
]