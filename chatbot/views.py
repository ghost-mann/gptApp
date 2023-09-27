from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer



# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hey this is my response'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
