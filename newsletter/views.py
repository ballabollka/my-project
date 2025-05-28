import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

UNISENDER_API_KEY = '6e5dmuk761steq47tteod6w5fzbc47spd5biat3a'
UNISENDER_LIST_ID = '3'  # строка, например '12345'

@csrf_exempt
def subscribe_newsletter(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Метод не поддерживается'}, status=405)
    try:
        data = json.loads(request.body)
        email = data.get('email')
        if not email:
            return JsonResponse({'error': 'Email не указан'}, status=400)

        # Отправляем подписку в UniSender без double opt-in
        payload = {
            'api_key': UNISENDER_API_KEY,
            'list_ids': UNISENDER_LIST_ID,
            'fields[email]': email,
            'double_optin': 0,  # без подтверждения, сразу подписка
            'overwrite': 2,
        }

        response = requests.post('https://api.unisender.com/ru/api/subscribe?format=json', data=payload)
        uni_data = response.json()

        if 'error' in uni_data:
            return JsonResponse({'error': uni_data['error']}, status=400)

        # Отправляем простое письмо "Спасибо за подписку"
        from django.core.mail import send_mail
        from django.conf import settings

        send_mail(
            subject='Спасибо за подписку!',
            message='Спасибо, что подписались на нашу рассылку! Мы будем присылать вам свежие новости.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=True,  # чтобы не падало если с почтой что-то
        )

        return JsonResponse({'message': 'Спасибо за подписку! Письмо отправлено на вашу почту.'})

    except Exception as e:
        return JsonResponse({'error': 'Ошибка сервера'}, status=500)
