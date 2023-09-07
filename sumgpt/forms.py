from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Upload

#サインアップ画面のフォームの生成
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#ログイン画面のフォームの生成
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='ユーザー名')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)


#文字起こし機能のファイルアップロード
class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('document',)