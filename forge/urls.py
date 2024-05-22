from django.urls import path, include
from rest_framework import routers
from .views import ForgeCourseViewSet, UpdateCourseStatus

router = routers.SimpleRouter()
router.register(r'course', ForgeCourseViewSet, basename='course')

urlpatterns = [
    path('status_update/<uuid:pk>/', UpdateCourseStatus.as_view(), name='status_update'),

]
urlpatterns += router.urls
