# from django.shortcuts import render
from rest_framework import viewsets
from .models import Courses, Category
from .serializers import CourseSerializer, CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
