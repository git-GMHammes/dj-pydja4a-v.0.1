from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.appsetor123_index,
        name='appsetor123_index'
    ),
    path(
        'cadastrar',
        views.appsetor123_cadastrar,
        name='appsetor123_cadastrar'
    ),
    path(
        'listar',
        views.appsetor123_listar,
        name='appsetor123_listar'
    ),
    path(
        'aualizar',
        views.appsetor123_atualizar,
        name='appsetor123_aualizar'
    ),
    path(
        'exclui',
        views.appsetor123_excluir,
        name='appsetor123_excluir'
    ),
    path(
        'insert',
        views.appsetor123_insert,
        name='appsetor123_insert'
    ),
    path(
        'read',
        views.appsetor123_read,
        name='appsetor123_read'
    ),
    path(
        'update',
        views.appsetor123_update,
        name='appsetor123_update'
    ),
    path(
        'delete',
        views.appsetor123_delete,
        name='appsetor123_delete'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
