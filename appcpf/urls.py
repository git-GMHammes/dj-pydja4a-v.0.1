from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.cpf_index,
        name='cpf_index'
    ),
    path(
        'listar',
        views.cpf_listar,
        name='cpf_listar'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
