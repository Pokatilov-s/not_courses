from django.urls import path, include
from rest_framework import routers
from .views import ForgeCourseViewSet

router = routers.DefaultRouter()
router.register(r'course', ForgeCourseViewSet)

urlpatterns = [

]
urlpatterns += router.urls
