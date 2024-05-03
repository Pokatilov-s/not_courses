from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializers import CourseSerializer
from .services import get_list_courses_owned_by_author


class ForgeCourseViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющий создавать, просматривать и редактировать курсы принадлежащие автору"""
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Создание курса с привязкой автора"""
        serializer.save(author_uuid=self.request.user)

    def get_queryset(self):
        """Получение списка курсов принадлежащих автору"""
        return get_list_courses_owned_by_author(self.request.user)

    def retrieve(self, request, *args, **kwargs):
        pass
    """Необходимо переопределить все методы """
