from django.urls import path
from django.contrib.auth import views as auth_views
from .view import auth, speech, SpeechRecognition, drive
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #サインアップ・ログイン機能
    #viewフォルダ内のauth.pyでviewを設定
    path("auth/signup", auth.signup, name="signup"),
    path("auth/login", auth.login_view, name="login"),
    path("auth/mypage", auth.mypage, name="mypage"),
    path("passchange", auth.passchange, name="passchange"),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path("speech", speech.index, name="speech"),
    path("SpeechRecognition", SpeechRecognition.index, name="SpeechRecognition"),
    path("sp", SpeechRecognition.sp, name="sp"),
    path('sum/<int:pk>/', SpeechRecognition.sum, name='sum'),
    path('sum_del/<int:pk>/', SpeechRecognition.sum_del, name='sumdel'),
    path('api/docx_download/', drive.docx_download, name='docxDownload'),
    path('api/docx_to_drive', drive.docx_to_drive, name='docxToDrive'),
]

#文字起こし機能のファイル削除用
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)