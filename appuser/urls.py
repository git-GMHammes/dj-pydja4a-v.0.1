from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.user_index,
        name='user_index'
    ),
    path(
        'logar',
        views.user_logar,
        name='user_logar'
    ),
    path(
        'autenticar',
        views.user_autenticar,
        name='user_autenticar'
    ),
    path(
        'deslogar',
        views.user_deslogar,
        name='user_deslogar'
    ),
    path(
        'listar',
        views.user_listar,
        name='user_listar'
    ),
    path(
        'cadastrar',
        views.user_cadastrar,
        name='user_cadastrar'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
