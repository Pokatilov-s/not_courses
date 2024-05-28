from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import (ReadOnlyCourseSerializer, ReadOnlyCategorySerializer, UserCourseSerializer,
                          CoursesAddedUserSerializer)
from store.servises.get_records_db import (get_list_published_courses, get_list_categories,
                                           get_list_courses_added_to_user)


class CategoriesViewSet(ReadOnlyModelViewSet):
    """API endpoint для получения объекта или списка объектов модели Category в режиме ReadOnly"""
    queryset = get_list_categories()
    serializer_class = ReadOnlyCategorySerializer


class CoursesReadOnlyViewSet(ReadOnlyModelViewSet):
    """API endpoint для получения объекта или списка объектов модели Course в режиме ReadOnly"""
    queryset = get_list_published_courses()
    serializer_class = ReadOnlyCourseSerializer


class AddCourseToUser(CreateAPIView):
    """API endpoint для добавления курсов пользователям"""
    serializer_class = UserCourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)


class CoursesAddedUser(ListAPIView):
    """API endpoint для получения списка курсов добавленных пользователю"""
    serializer_class = CoursesAddedUserSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_uuid = self.request.user.uuid
        return get_list_courses_added_to_user(user_uuid)

