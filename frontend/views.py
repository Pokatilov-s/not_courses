
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
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
