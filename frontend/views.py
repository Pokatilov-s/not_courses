from django.shortcuts import render

from forge.models import Category
from store.services import get_list_published_courses, get_list_categories


def index_store(request):
    courses = get_list_published_courses()
    categories = get_list_categories()
    return render(request, 'front/index_store.html', {'courses': courses, 'categories': categories})


def course_detail(request, course_uuid):
    course = get_list_published_courses(course_uuid)
    return render(request, 'front/course_detail.html', {'course': course})
