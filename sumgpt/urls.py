from django.urls import path
from django.contrib.auth import views as auth_views
from .view import auth
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #サインアップ・ログイン機能
    #viewフォルダ内のauth.pyでviewを設定
    path("auth/signup", auth.signup, name="signup"),
    path("auth/login", auth.login_view, name="login"),
    path("auth/mypage", auth.mypage, name="mypage"),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

]