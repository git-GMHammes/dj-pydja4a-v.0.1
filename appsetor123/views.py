from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Tab_model
from django.contrib import messages
# messages.add_message(request, messages.INFO, 'Aviso importante!!')

# Create your views here.


def appsetor123_index(request):
    return HttpResponse('Área reservada')


def appsetor123_cadastrar(request):
    if request.method != 'POST':
        messages.add_message(request, messages.INFO,
                             'Favor preencher o formulário!!')
        return render(request, 'appsetor123/setor123_cadastrar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        })
    # recebe = request.POST.get('')
    
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_listar(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_atualizar(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_excluir(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_insert(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_read(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_update(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })


def appsetor123_delete(request):
    return render(
        request,
        'appcomunica/modelo.html', {
            # Vazio
        })

# def com_funcao(request):
#     return render(
#         request,
#         'appcomunica/modelo.html', {
#             # Vazio
#         })
