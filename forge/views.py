from rest_framework import viewsets
from .models import Category, Course
from .serializers import CourseSerializer


class ForgeCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

