#google drive api関連の処理
from django.shortcuts import get_object_or_404
from ..models import Sum, Doc
import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from docx import Document  

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
        docs.Upload(param={'convert': True})
        #作成したファイルのURLを返す
        return 'https://docs.google.com/document/d/' + str(docs['id'])
    except:
        return "ERROR"

#wordファイルの作成関数
def create_wordfile(sum:Sum, filename):
    #wordファイルの文章構成は仮
    replace_dic = {"@要約文挿入@": sum.sum, "@原文挿入@" : sum.detail, "@ユーザー名挿入@" : sum.user, "@タイムスタンプ挿入@" : sum.timestamp.strftime('%Y/%m/%d %H:%M:%S')}
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    static_file_path = os.path.join(current_dir_path,'../static/template.docx')
    doc = Document(static_file_path)
    for i in range(len(doc.paragraphs)):
        if (doc.paragraphs[i].text == ""): continue
        if (doc.paragraphs[i].runs[0].underline == False): continue
        if(doc.paragraphs[i].runs[0].bold): continue
        for k, v in replace_dic.items():
            doc.paragraphs[i].text =  doc.paragraphs[i].text.replace(k, str(v).replace("\r", ""))
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    settings_file_path = os.path.join(current_dir_path,'../pydrive/{}.docx'.format(filename))
    doc.save(settings_file_path)

#sumをDocsに保存する
def save_sum_to_docs(filename, pk):
    sum = get_object_or_404(Sum, pk=pk)
    create_wordfile(sum, filename)
    return {"msg":"", "url": ""}
    content = "ユーザー名： {}\n要約文：\n{}\n本文：\n{}\nタイムスタンプ：\n{}".format(sum.user, sum.sum, sum.detail, sum.timestamp)
    docs_url = create_docs(filename, content)
    drive_msg = {"msg":"", "url": ""}
    if (docs_url == "ERROR"):
        drive_msg["msg"] = "GoogleDriveへの保存に失敗しました。"
    else:
        drive_msg["msg"] = "GoogleDriveへの保存に成功しました。"
        drive_msg["url"] = docs_url
        # DBの保存 
        Doc.objects.update_or_create(sum=sum, defaults={"url":docs_url})
    return drive_msg


