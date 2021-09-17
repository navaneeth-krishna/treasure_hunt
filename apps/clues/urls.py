from django.urls import path
from . import views

urlpatterns = [
    path("clues", views.clues, name="clues"),
    path("check", views.check, name="check"),
]
