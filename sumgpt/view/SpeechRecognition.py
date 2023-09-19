from django.shortcuts import render
import openai

def index(request):

    return render(request, 'sumgpt/SpeechRecognition.html')


from django.shortcuts import render

def sp(request):
    if request.method == 'POST':
        input_data = request.POST.get('data', '')


        openai.api_key = "32utDwbskjvX2F5_XYnuw3sgF60QgwqefnVF6ZNqbx0eJNLg2Uxi4oumhRLcrWFbELVrE3J6u76tn5YPnQXtGTw"
        openai.api_base = "https://api.openai.iniad.org/api/v1"

        question = '次の文章を簡潔に要約して\n' + input_data

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question},
            ],
        )
        speech_result = response['choices'][0]['message']['content']
        return render(request, 'sumgpt/sp.html', {'input_data': speech_result})
    else:
        return render(request, 'sumgpt/sp.html')
