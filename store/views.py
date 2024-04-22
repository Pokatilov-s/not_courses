from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from forge.models import Course, Category
from .serializers import ReadOnlyCourseSerializer, ReadOnlyCategorySerializer, UserCourseSerializer


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ReadOnlyCategorySerializer


class CoursesReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.filter(status='published')
    serializer_class = ReadOnlyCourseSerializer


class AddCourseToUser(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = UserCourseSerializer
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)
