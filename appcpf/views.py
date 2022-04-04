import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Tab_model

# Create your views here.


def cpf_index(request):
    return HttpResponse('Área reservada')


def cpf_listar(request):
    lista3 = ''
    recebe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    resultado = list(recebe)
    resposta = random.choice(list(recebe))

    lista2 = ['Linux', 'macOS', 'Windows']
    elemento = random.choice(lista2)
    
    return render(
        request,
        'appcpf/cpf_listar.html', {
            'elemento_html': lista2, 
            'lista_html': resultado,
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
    )


# def com_funcao(request):
#     return render(
#         request,
#         'appcomunica/modelo.html', {
#             # Vazio
#         }
#   )
