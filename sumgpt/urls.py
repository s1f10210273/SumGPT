from django.urls import path
from .view import auth
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #サインアップ・ログイン機能
    #viewフォルダ内のauth.pyでviewを設定
    path("auth/signup", auth.signup, name="signup"),
    path("auth/login", auth.login_view, name="login"),

]