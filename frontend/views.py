import time
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from store.services import get_list_published_courses, get_list_categories


def index_store(request):
    courses = get_list_published_courses()
    categories = get_list_categories()
    return render(request, 'front/index_store.html', {'courses': courses, 'categories': categories})


def course_detail(request, course_uuid):
    course = get_list_published_courses(course_uuid)
    return render(request, 'front/course_detail.html', {'course': course})


# Платёжка
def payment_page(request):
    course_info = request.session.get('course_info', {})
    return render(request, 'front/payment/payment.html', {'course_info': course_info})


@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        time.sleep(10)
        return JsonResponse({'status': 'success', 'message': 'Платеж успешно обработан!'})
    return JsonResponse({'status': 'error', 'message': 'Ошибка обработки платежа.'})


def success_page(request):
    return render(request, 'front/payment/success.html')
