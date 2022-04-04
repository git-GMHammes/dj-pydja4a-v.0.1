from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Tab_model

# Create your views here.

# def com_funcao(request):
#     return render(
#         request,
#         'appcomunica/modelo.html', {
#             # Vazio
#         })

def com_index(request):
    return HttpResponse('Área reservada')


def com_chat(request):
    # db_recebe = Tab_model.objects.all()
    return render(
        request,
        'appcomunica/com_comentario.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(),
        }
    )


def com_comentario(request):
    # db_recebe = Tab_model.objects.all()
    return render(
        request,
        'appcomunica/com_comentario.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(),
        }
    )


def com_avaliar(request):
    # db_recebe = Tab_model.objects.all()
    return render(
        request,
        'appcomunica/modelo.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(),
        }
    )


def com_curtir(request):
    # db_recebe = Tab_model.objects.all()
    return render(
        request,
        'appcomunica/modelo.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(),
        }
    )


def com_historico(request):
    # db_recebe = Tab_model.objects.all()
    return render(
        request,
        'appcomunica/modelo.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(),
        }
    )
