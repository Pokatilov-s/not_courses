from django.shortcuts import render
from store.services import get_list_published_courses


def index_store(request):
    courses = get_list_published_courses()
    return render(request, 'front/index_store.html', {'courses': courses})


def course_detail(request, course_uuid):
    course = get_list_published_courses(course_uuid)
    return render(request, 'front/course_detail.html', {'course': course})
