from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def payment_webhook(request):
    if request.method == 'POST':
        payment_id = request.data.get('payment_id')
        payment_status = request.data.get('status')

        print(payment_id)
        print(payment_status)

        return Response({'message': 'Статус платежа обновлён'}, status=200)
    return Response({'error': 'Не корректный запрос'}, status=400)  # Исправить описание ошибки
