from django.urls import path, include
from rest_framework import routers
from .views import ForgeCourseViewSet

router = routers.SimpleRouter()
router.register(r'course', ForgeCourseViewSet)

urlpatterns = [

]
urlpatterns += router.urls
