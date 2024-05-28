from django.urls import path
from .views import *

urlpatterns = [
    path('', index_store, name='index_store'),
    path('<uuid:course_uuid>/', course_detail, name='course_detail'),
    path('auth/', auth_page, name='auth_page'),
    path('my_courses/', my_courses_page, name='my_courses_page')
]
