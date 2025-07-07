from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def jogadores(request): 
    user_list = [
  {"nome": "Diego Alves", "posicao": "goleiro", "idade": 34, "nascimento": "Rio de Janeiro", "foto": "img/foto-diego-alves.jpg" },
  {"nome": "Rafinha", "posicao": "lateral-direito", "idade": 34, "nascimento": "Londrina" , "foto": "img/foto-rafinha.jpg"},
  {"nome": "Rodrigo Caio", "posicao": "zagueiro", "idade": 26, "nascimento": "Dracena" , "foto": "img/foto-rodrigo-caio.png"},
  {"nome": "Pablo Marí", "posicao": "zagueiro", "idade": 26, "nascimento": "Valência" , "foto": "img/foto-pablo-mari.jpg"},
  {"nome": "Filipe Luís", "posicao": "lateral-esquerdo", "idade": 34, "nascimento": "Jaraguá do Sul", "foto": "img/foto-felipe-luis.png"},
  {"nome": "Willian Arão", "posicao": "volante", "idade": 27, "nascimento": "São Paulo" , "foto": "img/foto-arao.jpg"},
  {"nome": "Gerson", "posicao": "meia", "idade": 22, "nascimento": "Rio de Janeiro" , "foto": "img/foto-gerson.jpg"},
  {"nome": "Éverton Ribeiro", "posicao": "meia", "idade": 30, "nascimento": "Arujá" , "foto": "img/foto-everton-ribeiro.jpg"},
  {"nome": "Arrascaeta", "posicao": "meia", "idade": 25, "nascimento": "Nuevo Berlín" , "foto": "img/foto-arrascaeta.jpg"},
  {"nome": "Bruno Henrique", "posicao": "atacante", "idade": 28, "nascimento": "Belo Horizonte" , "foto": "img/foto-bruno-henrique.jpg"},
  {"nome": "Gabigol", "posicao": "atacante", "idade": 23, "nascimento": "São Bernardo do Campo",   "foto": "img/foto-gabigol.jpg"},
  {"nome": "Jorge Jesus", "posicao": "tecnico", "idade": 70, "nascimento": "Amadora, Portugal",   "foto": "img/foto-jorge-jesus.png"},
  
]

    context = {
        "jogadores": user_list,  
    }
    return render(request, "jogadores.html", context)

def sobre(request):  
    return render(request, "sobre.html")