from django.urls import path
from . import views, auth

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/signup", auth.signup, name="signup"),
    path("auth/login", auth.login_view, name="login"),
]