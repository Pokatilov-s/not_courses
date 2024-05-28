from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from store.payment.serializers import PaymentSerializer
from store.serializers import TransactionsDetailsModelSerializer
from store.services.creating_records_to_db import enroll_user_in_course
from store.services.get_records_db import get_published_course, get_price_course
from store.services.validate_records_db import check_user_enrollment


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
    """API endpoint для обработки платёжа и добавления курса пользователю"""

    # Валидация входных данных
    serializer_pay = PaymentSerializer(data=request.data)
    if serializer_pay.is_valid():
        valid_data = serializer_pay.validated_data
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Ошибка валидации данных',
            'errors': serializer_pay.errors
        },
            status=400)

    # Проверка уникальности связи пользователя с курсом
    user = request.user
    if check_user_enrollment(user_uuid=user.uuid, course_uuid=valid_data.get('course_uuid')):
        return JsonResponse({
            'status': 'error',
            'message': 'Пользователь уже зарегистрирован на курс',
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
        # Создание связи пользователя с курсом с добавлением transaction_uuid
        enroll_user_in_course({
            'user_uuid': user.uuid,
            'course_uuid': transaction_data.get('course_uuid'),
            'transaction_uuid': transaction_uuid})

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


def success_page(request):
    """Вернуть страницу успешного платежа"""
    return render(request, 'payment/success.html')
