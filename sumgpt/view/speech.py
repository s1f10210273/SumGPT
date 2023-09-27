from django.shortcuts import render
from django.conf import settings
from ..forms import UploadForm
import openai
import os
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required

# .envファイルを読み込む
load_dotenv()

@login_required
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

            #以下要約機能。API叩くのめんどくさいから一回省略


            # openai.api_key = os.getenv("OPENAI_API_KEY")
            # openai.api_base = "https://api.openai.iniad.org/api/v1"

            # question = '次の文章を意味がわかるように簡潔に要約して\n' + text

            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         {"role": "user", "content": question},
            #     ],
            # )
            # speech_result = response['choices'][0]['message']['content']

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
