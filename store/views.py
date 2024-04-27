from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from forge.models import Course, Category
from .serializers import (ReadOnlyCourseSerializer, ReadOnlyCategorySerializer, UserCourseSerializer,
                          CoursesAddedUserSerializer)
from django.db import connection
from collections import namedtuple


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ReadOnlyCategorySerializer


class CoursesReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.filter(status='published')
    serializer_class = ReadOnlyCourseSerializer


class AddCourseToUser(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = UserCourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


class CoursesAddedUser(ListAPIView):
    serializer_class = CoursesAddedUserSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_uuid = self.request.user.uuid

        def named_tuple_fetchall(cursors):
            # "Return all rows from a cursor as a namedtuple"
            desc = cursors.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            return [nt_result(*row) for row in cursor.fetchall()]

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.* FROM user_courses us
                LEFT JOIN courses c
                ON c.uuid = us.course_uuid
                WHERE user_uuid = %s""", [user_uuid])
            rows = named_tuple_fetchall(cursor)

            return rows
