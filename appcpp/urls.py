from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.cpp_index,
        name='cpp_index'
    ),
    # path(
    #     '<int:id_app>',
    #     views.atualizar_app,
    #     name='atualizar_app'
    # )
]
