from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Tab_model

# Create your views here.


def appgeolocal_index(request):
    return HttpResponse('Área reservada')


# def com_funcao(request):
#     return render(
#         request,
#         'appcomunica/modelo.html', {
#             # Vazio
#         })

