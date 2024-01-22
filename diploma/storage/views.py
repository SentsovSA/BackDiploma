import logging

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from random import randint as random
from storage.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

client = []
event = None
client_send = []
response = []


def home(request):
    return render(request, "index.html")


@csrf_exempt
def login(request):
    global client, event, client_send, response

    if request.method == 'POST':
        jsonRequest = json.loads(request.body)
        method = jsonRequest['method']
        print(method)

        if method is not None:
            if method == 'register':
                email = jsonRequest['email']
                code = random(10000, 90000)
                send_mail(
                    'Код подтверждения',
                    f'Код подтверждения для регистрации в сервисе CarApp {code}',
                    'car.app@mail.ru',
                    [email],
                    fail_silently=False,
                )
                response = {"response": "confirmation", "code": str(code)}
                print(response)

            elif method == 'confirm':
                email = str(request.POST.get('email'))
                password = str(request.POST.get('pass'))
                name = str(request.POST.get('name'))
                phone = str(request.POST.get('phone'))
                User.objects.create(userName=name, userEmail=email, userPhone=phone, userPassword=password)
                user = User.objects.get(userEmail=email)
                response = {"response": user.userID}

            elif method == 'login':
                email = str(request.POST.get('email'))
                password = str(request.POST.get('pass'))
                user = User.objects.get(userEmail=email)
                if user.userPassword == password:
                    response = {"response": user.userID}
                else:
                    response = {"response": 'error', "error_code": 201}
        else:
            response = {'Response': 404}

    elif request.method == 'GET':
        method = request.GET.get('method')

        if method is not None:
            if method == 'get_client_name':
                client_name = random(1000, 9000)
                if client_name in client:
                    client_name = random(1000, 9000)
                if str(client_name) not in str(client):
                    client.append(client_name)
                response = {"client_name": client_name}

            elif method == 'update':
                client_name = request.GET.get('client_name')
                array = {"client_name": client_name, "update": []}
                if event is not None:
                    if client_name not in client_send:
                        array['update'].append(event)
                        client_send.append(client_name)
                    if len(client) == len(client_send):
                        event = None
                        client_send = []
                response = array

            elif method == 'message':
                message = request.GET.get('message')
                user_id = request.GET.get('user_id')
                user = User.objects.get(userID=user_id)
                event = {"type": "message_now", "message": message, "peer_id": user_id, "name": user.userName}
                response = {"Response": 200}

            elif method == 'quit':
                client_name = int(request.GET.get('client_name'))
                for i in range(len(client)):
                    if client_name == client[i]:
                        del client[i]
                response = {"Response": 200}

        else:
            response = {'Response': 404}

    print(response['code'])
    return JsonResponse(data=response['code'], safe=False)
