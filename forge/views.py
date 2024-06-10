from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CourseSerializer, StatusCourseSerializer
from forge.services.get_records import get_list_courses_owned_by_author, get_courses_owned_by_author


class ForgeCourseViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющий создавать, просматривать и редактировать курсы принадлежащие автору"""
    serializer_class = CourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('status', 'category', 'price', 'created_at', 'updated_at', 'students_qty', 'reviews_qty')
    search_fields = ('title', 'description')
    ordering_fields = ('status', 'category', 'price', 'created_at', 'updated_at', 'students_qty', 'reviews_qty')

    def perform_create(self, serializer):
        """Создание курса с привязкой автора"""
        serializer.save(author_uuid=self.request.user)

    def get_queryset(self):
        """Получение списка курсов принадлежащих автору"""
        return get_list_courses_owned_by_author(self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """Получение курса принадлежащего втору"""
        # Используется метод retrieve родительского класса RetrieveModelMixin
        # фильтрует полученный queryset из get_queryset что может быть не очень эффективно,
        # но при этом выполняется условие валидации, автор может получить только принадлежащий ему курс.
        # При необходимости оптимизации запросов добавить выше описанную валидацию.
        return super().retrieve(request, *args, **kwargs)


class UpdateCourseStatus(generics.UpdateAPIView):
    """API endpoint дял изменения статуса курса"""
    serializer_class = StatusCourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def partial_update(self, request, *args, **kwargs):
        course = get_courses_owned_by_author(user=self.request.user, pk=kwargs.get('pk'))
        serializer = self.serializer_class(course, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        # Заглушка на PUT метод
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'detail': 'Метод PUT не разрешён'})
