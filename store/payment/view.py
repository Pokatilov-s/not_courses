from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from store.payment.serializers import PaymentSerializer
from store.serializers import TransactionsDetailsModelSerializer
from store.services import get_published_course, get_price_course


def payment_page(request):
    """Сформировать платёжную страницу"""
    course_uuid = request.GET.get('uuid')
    course = get_published_course(uuid=course_uuid)
    course_info = {
        'uuid': course.uuid,
        'name': course.title,
        'price': course.price
    }
    return render(request, 'payment/payment.html', {'course_info': course_info})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def process_payment(request):
    """Обработать платёж и добавить курс пользователю"""

    # Валидация входных данных
    serializer_pay = PaymentSerializer(data=request.data)
    if serializer_pay.is_valid():
        # user = request.user
        valid_data = serializer_pay.validated_data
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Ошибка валидации данных',
            'errors': serializer_pay.errors
        },
            status=400)

    # Подготовка данных для создания объекта модели TransactionsDetail
    transaction_data = {
        'course_uuid': valid_data.get('course_uuid'),
        'price': get_price_course(valid_data.get('course_uuid')),
        'bank': valid_data.get('bank')
    }
    serializer_transaction = TransactionsDetailsModelSerializer(data=transaction_data)

    # Создание объекта модели TransactionsDetail
    if serializer_transaction.is_valid():
        transaction = serializer_transaction.save()
        transaction_uuid = transaction.uuid
        return JsonResponse({
            'status': 'success',
            'message': 'Платеж успешно обработан!',
            'transaction_id': transaction_uuid
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Ошибка обработки платежа.',
            'errors': serializer_transaction.errors
        },
            status=400)


# def add_user_course(user, transaction, data):
#     # Добавление курса пользователю
#     user_course_data = {
#
#         'course_uuid': data.get('course_uuid')
#     }
#     serializer_user_course = UserCourseSerializer()

def success_page(request):
    return render(request, 'payment/success.html')
