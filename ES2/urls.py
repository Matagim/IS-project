from django.urls import path  
from . import views

app_name = "ES2"
urlpatterns = [
    path("home", views.index, name="home"),
    path("Exercícios", views.Exercicio, name="Exercicio"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("Invitation", views.Invitation_view, name="Invitation")
]