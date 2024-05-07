from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CourseSerializer
from .services import get_list_courses_owned_by_author
from .models import Course


class ForgeCourseViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющий создавать, просматривать и редактировать курсы принадлежащие автору"""
    serializer_class = CourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Создание курса с привязкой автора"""
        serializer.save(author_uuid=self.request.user)

    def get_queryset(self):
        """Получение списка курсов принадлежащих автору"""
        status = self.request.query_params.get('status')
        return get_list_courses_owned_by_author(self.request.user, status=status)

    def retrieve(self, request, *args, **kwargs):
        """Получение курса принадлежащего втору"""
        # Используется метод retrieve родительского класса RetrieveModelMixin
        # фильтрует полученный queryset из get_queryset что может быть не очень эффективно,
        # но при этом выполняется условие валидации, автор может получить только принадлежащий ему курс.
        # При необходимости оптимизации запросов добавить выше описанную валидацию.
        return super().retrieve(request, *args, **kwargs)



