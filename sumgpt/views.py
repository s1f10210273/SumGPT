from django.shortcuts import render, redirect, get_object_or_404#404のみshow
from django.conf.urls.static import static
from django.conf import settings #MEDIA_ROOT等にアクセスする際に必要

#=============show===============-
from .models import WordCloud_test, WordCloud_m
#==============gen=================-
from .word_cloud_M import WC #外で定義した関数を使って既存fileの文字列を画像へ変換)
#==============gen=================-

# Create your views here.
def index(request):
    return render(request, "sumgpt/index.html")

#generate_wordcloudはSppech.pyでテキスト形式のものをwordcloudにするため不要になった。
#既存ファイル（名）からワードクラウドを作成する。
#再利用できるかもしれないと思って取ってある。けれど、今のところ不要。

def generate_wordcloud(request):#こちらで使うモジュールはgenで囲む。
    # WordCloudを生成する
    input = f"{settings.BASE_DIR}\sumgpt\sample.txt"#ここで使用する文字ファイルを固定している。ここだけ書き換えれば別ファイルも使用可。
    id = WC(input)
    return  redirect('show_wordcloud_M', id)

def show_wordcloud_M(request, id): #idに対するWordCloud_testのインスタンスを取得
    wc_file = get_object_or_404(WordCloud_test, id=id)
    context = {
        'wc' : wc_file
    }
    return render(request, "sumgpt/wordcloud.html", context)

def show_wordcloud(request, id): #idに対するWordCloud_mのインスタンスを取得(本番の画像生成を確認するための関数)
    wc_file = get_object_or_404(WordCloud_m, id=id)
    context = {
        'wc' : wc_file
    }
    return render(request, "sumgpt/wordcloud.html", context)