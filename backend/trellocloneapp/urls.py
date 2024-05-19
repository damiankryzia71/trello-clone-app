from django.urls import path
from . import views

urlpatterns = [
    path("create-board/", views.create_board)
]