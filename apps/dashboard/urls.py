from django.urls import path
from . import views

urlpatterns = [
    path("guidelines", views.guidelines, name="guidelines"),
]
