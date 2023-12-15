from django.urls import path
from django.contrib.auth import views as auth_views
from .view import auth, speech, SpeechRecognition
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
    path('generate_wordcloud', views.generate_wordcloud, name="generate_wordcloud"), #再利用用。おそらく本番は使用しない。詳しくはviews
    path('test_wordcloud/<int:id>/', views.show_wordcloud_M, name="show_wordcloud_M"), #wordcloudテスト用モデルのid。指定されたidの画像を表示する。
    path('wordcloud/<int:id>/', views.show_wordcloud, name="show_wordcloud") #wordcloud用モデルのid。指定されたidの画像を表示する。
]

#文字起こし機能のファイル削除用
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)