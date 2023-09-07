from django.shortcuts import render,redirect
from django.conf import settings
from ..forms import UploadForm

def index(request):
    import os
    import subprocess

    #保存PATH
    source = "/upload/"

    #結果保存
    speech_result = ""

    if request.method == 'POST':
        # アップロードファイルの保存
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.save()
            transcribe_file = os.path.join(settings.MEDIA_ROOT, upload.document.name)
            name, ext = os.path.splitext(transcribe_file)

        if ext==".wav":
            #文字起こし
            #pip install SpeechRecognition
            import speech_recognition as sr
            r = sr.Recognizer()
            with sr.AudioFile(transcribe_file) as source:
                audio = r.record(source)
            text = r.recognize_google(audio, language='ja-JP')
            speech_result = text

        else:
            speech_result = "wavファイルのみ"

        transcribe_file_path = upload.document.path

        # 作業用ファイルの削除
        cmd = 'rm -f ' + transcribe_file_path
        subprocess.call(cmd, shell=True)

    else:
        form = UploadForm()
    return render(request, 'sumgpt/speech.html', {
        'form': form,
        'transcribe_result':speech_result
    })
