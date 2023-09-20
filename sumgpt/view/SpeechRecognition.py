from django.shortcuts import render, get_object_or_404
from ..models import Sum
import openai
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

def index(request):

    return render(request, 'sumgpt/SpeechRecognition.html')


def sp(request):
    if request.method == 'POST':
        input_data = request.POST.get('data', '')


        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_base = "https://api.openai.iniad.org/api/v1"

        question = '次の文章を簡潔に要約して\n' + input_data

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question},
            ],
        )
        speech_result = response['choices'][0]['message']['content']

        # データを保存
        user = request.user
        Sum.objects.create(user=user, sum=speech_result)

        return render(request, 'sumgpt/sp.html', {'input_data': speech_result})
    else:
        return render(request, 'sumgpt/sp.html')


def sum(request, pk):
    sum_data = get_object_or_404(Sum, pk=pk)  # SumモデルとデータのIDを指定
    return render(request, 'sumgpt/sum.html', {'sum_data': sum_data})
