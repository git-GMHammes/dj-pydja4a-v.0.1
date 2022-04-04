from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Tab_model

# Create your views here.


def user_index(request):
    return HttpResponse('Área reservada')


def user_logar(request):
    return render(
        request,
        'appuser/user_logar.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(), 
        })


def user_autenticar(request):
    return render(
        request,
        'appuser/user_autenticar.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(), 
        })


def user_deslogar(request):
    return render(
        request,
        'appuser/user_deslogar.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(), 
        })


def user_listar(request):
    return render(
        request,
        'appuser/user_listar.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(), 
        })


def user_cadastrar(request):
    return render(
        request,
        'appuser/user_cadastrar.html', {
            'url1' : request.build_absolute_uri(), 
            'url2' : request.get_full_path(), 
        })
