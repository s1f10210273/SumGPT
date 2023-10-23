#google drive api関連の処理
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Sum
import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from django.contrib.auth.decorators import login_required

def access_drive():
    #Google認証
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    settings_file_path = os.path.join(current_dir_path,'../pydrive/settings.yaml')
    gauth = GoogleAuth(settings_file=settings_file_path)
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

#Docsの新規作成保存
def create_docs(title, content):
    drive = access_drive()
    docs = drive.CreateFile({'title': title})
    docs.SetContentString(content)
    #作成したファイルの情報を表示
    print(docs)
    #ファイルのアップロード(google driveの最上位のディレクトリに置かれます。)
    docs.Upload()

#sumをDocsに保存する
@login_required
def save_sum_to_docs(request, pk, title = "sumGPT"):
    sum_data = get_object_or_404(Sum, pk=pk)
    content = "ユーザー名:{}\n要約文:\n{}本文:\n{}\nタイムスタンプ\n{}".format(sum_data.user, sum_data.sum, sum_data.detail, sum_data.timestamp)
    create_docs(title, content)
    return render(request, 'sumgpt/sum.html', {'sum_data': sum_data})

