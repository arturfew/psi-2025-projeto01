from django.shortcuts import render
from blog.models import Post 

def jogadores(request):
    posts = Post.objects.all().order_by('data_publicacao')  # pega todos os posts
    return render(request, 'app/jogadores.html', {'posts': posts})


def inicio(request):
    return render(request, "app/inicio.html")



def sobre(request): 
    titulos_list = [
    {"titulo":"Campeonato Brasileiro Série A - Campeão com 90 pontos"},
    {"titulo":"Copa Libertadores da América - Campeão invicto na fase final"},
    {"titulo":"Carioca - Campeão Estadual"},
    {"titulo":"Supercopa do Brasil - Campeão disputada em 2020, referente a 2019"},
    ] 

    context = {
        "sobre": titulos_list,
    }
    return render(request, "app/sobre.html", context)
    


 