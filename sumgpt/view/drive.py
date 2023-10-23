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
def create_docs(filename, content):
    drive = access_drive()
    docs = drive.CreateFile({'title': filename, 'mimeType':	"application/vnd.openxmlformats-officedocument.wordprocessingml.document"})
    docs.SetContentString(content)
    #ファイルのアップロード(google driveの最上位のディレクトリに置かれます。)
    docs.Upload()
    #作成したファイルの情報を表示
    #print(docs)

#sumをDocsに保存する
@login_required
def save_sum_to_docs(request):
    if request.method == 'POST':
        filename = request.POST.get("filename", None)        
        pk = request.POST.get("pk", None)
        sum_data = get_object_or_404(Sum, pk=pk)
        content = "ユーザー名： {}\n要約文：\n{}\n本文：\n{}\nタイムスタンプ：\n{}".format(sum_data.user, sum_data.sum, sum_data.detail, sum_data.timestamp)
        create_docs(filename, content)
        return render(request, 'sumgpt/sum.html', {'sum_data': sum_data})
    else:
        return redirect('mypage')

