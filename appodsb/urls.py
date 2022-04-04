from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.appodsb_index,
        name='appodsb_index'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
