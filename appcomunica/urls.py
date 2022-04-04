from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.com_index,
        name='com_index'
    ),
    path(
        'chat',
        views.com_chat,
        name='com_chat'
    ),
    path(
        'comentario',
        views.com_comentario,
        name='com_comentario'
    ),
    path(
        'avaliacao',
        views.com_avaliar,
        name='com_avaliar'
    ),
    path(
        'curtir',
        views.com_curtir,
        name='com_curtir'
    ),
    path(
        'curtir',
        views.com_historico,
        name='com_historico'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
