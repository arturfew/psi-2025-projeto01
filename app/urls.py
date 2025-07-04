from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),# rota para "/
    path('sobre/', views.sobre, name='sobre'),
    path('jogadores/', views.jogadores, name='jogadores'),  
]