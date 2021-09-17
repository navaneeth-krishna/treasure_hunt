from django.urls import path
from . import views

urlpatterns = [
    path("q1", views.q1, name="q1"),
    path("q2", views.q2, name="q2"),
]
