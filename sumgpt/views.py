from django.shortcuts import render, redirect, get_object_or_404#404のみshow
from django.conf.urls.static import static
from django.conf import settings #MEDIA_ROOT等にアクセスする際に必要

#=============show===============-
from .models import WordCloud_test
#==============gen=================-
from .word_cloud_M import WC #外で定義した関数を使って既存fileの文字列を画像へ変換)
#==============gen=================-

# Create your views here.
def index(request):
    return render(request, "sumgpt/index.html")

def generate_wordcloud(request):#こちらで使うモジュールはgenで囲む。

    # WordCloudを生成する
    input = f"{settings.BASE_DIR}\sumgpt\sample.txt"
    id = WC(input)
    return  redirect('show_wordcloud', id)

def show_wordcloud(request, id): #idに対するWordCloudのインスタンスを取得
    wc_file = get_object_or_404(WordCloud_test, id=id)
    context = {
        'wc' : wc_file
    }
    #create_path = word_cloud.WC("static/sumget/text/sample.txt", "")
    #↑以外は、単にデータベースに保存された画像をhtmlいっぱいに表示する関数。
    return render(request, "sumgpt/wordcloud.html", context)