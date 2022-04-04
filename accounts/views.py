from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Tab_model
from django.contrib import messages
# messages.add_message(request, messages.INFO, 'Aviso importante!!')
# from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.


def count_index(request):
    return HttpResponse('Área reservada')


def count_logar(request):

    return render(
        request,
        'accounts/count_logar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
    )


def count_autenticar(request):
    return render(
        request,
        'accounts/count_autenticar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
    )


def count_deslogar(request):
    return render(
        request,
        'accounts/count_deslogar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
    )


def count_listar(request):
    return render(
        request,
        'accounts/count_listar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
    )


def count_cadastrar(request):
    if request.method != 'POST':
        messages.add_message(request, messages.INFO,
                             'Favor preencher o formulário!!')
        return render(request, 'accounts/count_cadastrar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        })
    # recebe = request.POST.get('')
    campo_nome_completo = request.POST.get('campo_nome_completo')
    campo_aceito_check = request.POST.get('campo_aceito_check')
    campo_referencia = request.POST.get('campo_referencia')
    campo_password1 = request.POST.get('campo_password1')
    campo_password2 = request.POST.get('campo_password2')
    campo_endereco = request.POST.get('campo_endereco')
    campo_username = request.POST.get('campo_username')
    campo_numero = request.POST.get('campo_numero')
    campo_bairro = request.POST.get('campo_bairro')
    campo_cidade = request.POST.get('campo_cidade')
    campo_email = request.POST.get('campo_email')
    campo_cpf = request.POST.get('campo_cpf')
    campo_cep = request.POST.get('campo_cep')
    campo_rg = request.POST.get('campo_rg')
    campo_uf = request.POST.get('campo_uf')
    # INICIO DAS VALIDAÇÕES
    if not campo_nome_completo or not campo_username:
        messages.add_message(request, messages.ERROR, 'O Formulário possui campo vazio')
        return render(request, 'accounts/count_cadastrar.html', {
            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
        )
    #
    try:
        validate_email(campo_email)
    except ValidationError as e:
        messages.add_message(request, messages.ERROR, e)
    #
    #
    # FINAL DAS VALIDAÇÕES
    #
    return render(
        request,
        'accounts/count_cadastrar.html', {

            'url1': request.build_absolute_uri(),
            'url2': request.get_full_path(),
        }
    )
