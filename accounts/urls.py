from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.count_index,
        name='count_index'
    ),
    path(
        'logar',
        views.count_logar,
        name='count_logar'
    ),
    path(
        'autenticar',
        views.count_autenticar,
        name='count_autenticar'
    ),
    path(
        'deslogar',
        views.count_deslogar,
        name='count_deslogar'
    ),
    path(
        'listar',
        views.count_listar,
        name='count_listar'
    ),
    path(
        'cadastrar',
        views.count_cadastrar,
        name='count_cadastrar'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
