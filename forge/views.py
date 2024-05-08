from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import CourseSerializer, StatusCourseSerializer
from .services import get_list_courses_owned_by_author, get_courses_owned_by_author


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
        status_curse = self.request.query_params.get('status')
        return get_list_courses_owned_by_author(self.request.user, status=status_curse)

    def retrieve(self, request, *args, **kwargs):
        """Получение курса принадлежащего втору"""
        # Используется метод retrieve родительского класса RetrieveModelMixin
        # фильтрует полученный queryset из get_queryset что может быть не очень эффективно,
        # но при этом выполняется условие валидации, автор может получить только принадлежащий ему курс.
        # При необходимости оптимизации запросов добавить выше описанную валидацию.
        return super().retrieve(request, *args, **kwargs)


class UpdateCourseStatus(generics.UpdateAPIView):
    serializer_class = StatusCourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def partial_update(self, request, *args, **kwargs):
        course = get_courses_owned_by_author(user=self.request.user, pk=kwargs.get('pk'))
        serializer = self.serializer_class(course, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
