
from django.urls import path
from . import views

urlpatterns = [
    # URL para a lista de todos os posts (index do blog)
    path('', views.post_list, name='post_list'),
    path('info/', views.info_list, name='info_list'),
    
]