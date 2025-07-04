from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('jogadores/', views.jogadores, name='jogadores'),
    path('sobre/', views.sobre, name='sobre'),
]