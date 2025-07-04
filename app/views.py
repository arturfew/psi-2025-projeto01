from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def jogadores(request): 
    user_list = [
        {"nome": "Jole Pedro", "matricula": "0003", "idade": 17, "cidade": "Riachuelo"},
        {"nome": "Nudson", "matricula": "0002", "idade": 17, "cidade": "Boa Saúde"},
        {"nome": "Jole Filho", "matricula": "0003", "idade": 18, "cidade": "Sarra Cidade"},
        {"nome": "Artur", "matricula": "0004", "idade": 17, "cidade": "Santa Maria"},
        {"nome": "Murillo", "matricula": "0005", "idade": 17, "cidade": "São Tomé"},
    ]
    context = {
        "jogadores": user_list,  
    }
    return render(request, "jogadores.html", context)

def sobre(request):  
    return render(request, "sobre.html")