from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "inicio.html")

def jogadores(request):
    user_list = [
        {"nome": "João Pedro", "matricula": "0001", "idade": 17, "cidade": "Riachuelo"},
        {"nome": "Hudson", "matricula": "0002", "idade": 17, "cidade": "Boa Saúde"},
        {"nome": "joão filho", "matricula": "0003", "idade": 18, "cidade": "Serra Caiada"},
        {"nome": "Artur", "matricula": "0004", "idade": 17, "cidade": "Santa Maria"},
        {"nome": "Murilo", "matricula": "0005", "idade": 17, "cidade": "são tome"},
    ]
            
    context = {
        "jogadores": user_list,
    }
    return render(request, "jogadores.html", context)
            

def sobre(request):
    return render(request, "sobre.html")