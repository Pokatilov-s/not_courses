from rest_framework import viewsets


from forge.models import Course, Category
from .serializers import ReadOnlyCourseSerializer, ReadOnlyCategorySerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ReadOnlyCategorySerializer


class CoursesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.filter(status='published')
    serializer_class = ReadOnlyCourseSerializer
