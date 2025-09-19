from django.shortcuts import render
from blog.models import Post, Info

def jogadores(request):
    posts = Post.objects.all().order_by('data_publicacao')  # pega todos os posts
    return render(request, 'app/jogadores.html', {'posts': posts})


def inicio(request):
    return render(request, "app/inicio.html")


def sobre(request):
    infos = Info.objects.all().order_by('data_publicacao')  # pega todos os posts
    return render(request, "app/sobre.html" , {'infos': infos})

 