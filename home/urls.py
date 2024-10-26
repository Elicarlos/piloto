from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    path('sobre/', views.sobre, name="sobre")
]