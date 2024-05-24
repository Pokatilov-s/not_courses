from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from forge.models import Course
from store.payment.serializers import PaymentSerializer


# Платёжка
def payment_page(request):
    """Сформировать платёжную страницу"""
    course_uuid = request.GET.get('uuid')
    course = get_object_or_404(Course, uuid=course_uuid)
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
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        valid_data = serializer.validated_data

        return JsonResponse({'status': 'success', 'message': 'Платеж успешно обработан!'})
    return JsonResponse({
        'status': 'error',
        'message': 'Ошибка валидации данных',
        'errors': serializer.errors}, status=400)
    # return JsonResponse({'status': 'error', 'message': 'Ошибка обработки платежа.'})


def success_page(request):
    return render(request, 'payment/success.html')
