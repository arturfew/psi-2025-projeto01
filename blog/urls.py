
from django.urls import path
from . import views

urlpatterns = [
    # URL para a lista de todos os posts (index do blog)
    path('', views.post_list, name='post_list'),

    # URL para a página de um post específico (ex: /blog/post/5/)
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]