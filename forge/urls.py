from django.urls import path, include
from rest_framework import routers
from .views import ForgeCourseViewSet

router = routers.SimpleRouter()
router.register(r'course', ForgeCourseViewSet, basename='course')

urlpatterns = [

]
urlpatterns += router.urls
