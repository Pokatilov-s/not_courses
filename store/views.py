from rest_framework import viewsets


from forge.models import Course, Category
from .serializers import CourseSerializer, CategorySerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CoursesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
