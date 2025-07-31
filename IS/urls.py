from django.urls import path  
from . import views

app_name = "IS"
urlpatterns = [
    path('front_page', views.front_page_loader, name="front_page"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name="logout"),
    path('home', views.home_page, name="home")
]