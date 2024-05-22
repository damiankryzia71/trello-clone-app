from django.urls import path
from . import views

urlpatterns = [
    path("createBoard/", views.create_board),
    path("registerAccount/", views.register_account),
    path("createCard/", views.create_card),
    path("addColorTag/", views.add_color_tag),
    path("moveCard/", views.move_card),
    path("getBoards/", views.get_boards)
]