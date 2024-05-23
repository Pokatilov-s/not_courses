import time
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from forge.models import Course
from store.services import get_list_published_courses, get_list_categories


def index_store(request):
    courses = get_list_published_courses()
    categories = get_list_categories()
    return render(request, 'front/index_store.html', {'courses': courses, 'categories': categories})


def course_detail(request, course_uuid):
    course = get_list_published_courses(course_uuid)
    return render(request, 'front/course_detail.html', {'course': course})


# Авторизация и Регистрация
def auth_page(request):
    return render(request, 'front/auth/auth.html')


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
    return render(request, 'front/payment/payment1.html', {'course_info': course_info})


# @csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        time.sleep(10)
        n = request.body.decode('UTF-8')
        print(n)

        return JsonResponse({'status': 'success', 'message': 'Платеж успешно обработан!'})
    return JsonResponse({'status': 'error', 'message': 'Ошибка обработки платежа.'})


def success_page(request):
    return render(request, 'front/payment/success.html')
