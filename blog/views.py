from django.shortcuts import render
from .models import Post
from .models import Info

# Esta é a função que estava faltando!
def post_list(request):
# Esta linha busca todos os objetos Post no banco de dados, ordenando pelos mais recentes
    posts = Post.objects.all().order_by('-data_publicacao')
# Esta linha renderiza o template HTML, passando a lista de posts para ele
    return render(request, 'blog/post_list.html', {'posts': posts})

def info_list(request):
    infos = Info.objects.all().order_by('-data_publicacao')
    return render(request, 'blog/info_list.html', {'infos': infos})







 


