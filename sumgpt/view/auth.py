from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from ..forms import UserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


#サインアップ・ログイン機能


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth/signup')
    else:
        form = UserForm()
    return render(request, 'sumgpt/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'sumgpt/login.html', {'form': form})



@login_required
def mypage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # セッションの認証ハッシュを更新
            messages.success(request, 'パスワードが変更されました。')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'sumgpt/mypage.html', {'form': form})