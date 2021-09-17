from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.login, name="login"),  # Homepage is the login screen
    path("register", views.register, name='register'),
    re_path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("editprofile", views.editprofile, name='editprofile'),
]
