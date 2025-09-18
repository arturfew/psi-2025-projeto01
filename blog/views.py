from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post

# Esta é a função que estava faltando!
def post_list(request):
# Esta linha busca todos os objetos Post no banco de dados, ordenando pelos mais recentes
    posts = Post.objects.all().order_by('-data_publicacao')
# Esta linha renderiza o template HTML, passando a lista de posts para ele
    return render(request, 'blog/post_list.html', {'posts': posts})

# Esta função será usada pela outra URL, para mostrar um post individual
def post_detail(request, pk):
# Esta linha busca o post com o ID (pk) específico, ou mostra um erro 404 se não encontrar
    post = get_object_or_404(Post, pk=pk)
# Esta linha renderiza o template de detalhe, passando o post específico
    return render(request, 'blog/post_detail.html', {'post': post})

# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Info

# Esta é a função que estava faltando!
def post_list(request):
    # Esta linha busca todos os objetos Post no banco de dados, ordenando pelos mais recentes
    posts = Post.objects.all().order_by('-data_publicacao') 
    # Esta linha renderiza o template HTML, passando a lista de posts para ele
    return render(request, 'blog/post_list.html', {'posts': posts})


 


