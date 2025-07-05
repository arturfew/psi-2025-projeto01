from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def jogadores(request): 
    user_list = [
  {"nome": "Diego Alves", "posicao": "goleiro", "idade": 34, "nascimento": "Rio de Janeiro"},
  {"nome": "Rafinha", "posicao": "lateral-direito", "idade": 34, "nascimento": "Londrina"},
  {"nome": "Rodrigo Caio", "posicao": "zagueiro", "idade": 26, "nascimento": "Dracena"},
  {"nome": "Pablo Marí", "posicao": "zagueiro", "idade": 26, "nascimento": "Valência"},
  {"nome": "Filipe Luís", "posicao": "lateral-esquerdo", "idade": 34, "nascimento": "Jaraguá do Sul"},
  {"nome": "Willian Arão", "posicao": "volante", "idade": 27, "nascimento": "São Paulo"},
  {"nome": "Gerson", "posicao": "meia", "idade": 22, "nascimento": "Rio de Janeiro"},
  {"nome": "Éverton Ribeiro", "posicao": "meia", "idade": 30, "nascimento": "Arujá"},
  {"nome": "Arrascaeta", "posicao": "meia", "idade": 25, "nascimento": "Nuevo Berlín"},
  {"nome": "Bruno Henrique", "posicao": "atacante", "idade": 28, "nascimento": "Belo Horizonte"},
  {"nome": "Gabigol", "posicao": "atacante", "idade": 23, "nascimento": "São Bernardo do Campo"}
]

    context = {
        "jogadores": user_list,  
    }
    return render(request, "jogadores.html", context)

def sobre(request):  
    return render(request, "sobre.html")