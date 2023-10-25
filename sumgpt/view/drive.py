#google drive api関連の処理
from django.shortcuts import get_object_or_404
from ..models import Sum
import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def access_drive():
    #Google認証
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    settings_file_path = os.path.join(current_dir_path,'../pydrive/settings.yaml')
    gauth = GoogleAuth(settings_file=settings_file_path)
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

#Docsの新規作成保存
def create_docs(filename, content):
    try:
        drive = access_drive()
        docs = drive.CreateFile({'title': filename, 'mimeType':	"text/plain"})
        docs.SetContentString(content)
        #ファイルのアップロード(google driveの最上位のディレクトリに置かれます。)
        print("_")
        docs.Upload(param={'convert': True})
        print("4")
        #作成したファイルのURLを返す
        return 'https://docs.google.com/document/d/' + str(docs['id'])
    except:
        return "ERROR"

#sumをDocsに保存する
def save_sum_to_docs(filename, pk):
    sum_data = get_object_or_404(Sum, pk=pk)
    content = "ユーザー名： {}\n要約文：\n{}\n本文：\n{}\nタイムスタンプ：\n{}".format(sum_data.user, sum_data.sum, sum_data.detail, sum_data.timestamp)
    docs_url = create_docs(filename, content)
    drive_msg = {"msg":"", "url": ""}
    if (docs_url == "ERROR"):
        drive_msg["msg"] = "GoogleDriveへの保存に失敗しました。"
    else:
        drive_msg["msg"] = "GoogleDriveへの保存に成功しました。"
    return drive_msg

