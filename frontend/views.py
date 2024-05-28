from django.shortcuts import render
from store.services.get_records_db import get_list_published_courses, get_list_categories, get_published_course


def index_store(request):
    courses = get_list_published_courses()
    categories = get_list_categories()
    return render(request, 'front/index_store.html', {'courses': courses, 'categories': categories})


def course_detail(request, course_uuid):
    course = get_published_course(uuid=course_uuid)
    return render(request, 'front/course_detail.html', {'course': course})


# Авторизация и Регистрация
def auth_page(request):
    return render(request, 'front/auth/auth.html')


# курсы пользователя
def my_courses_page(request):
    return render(request, 'front/my_courses.html')
