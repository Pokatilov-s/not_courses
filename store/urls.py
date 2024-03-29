from rest_framework import routers
from django.urls import path, include
from .views import CoursesViewSet, CategoriesViewSet

router = routers.SimpleRouter()
router.register(r'courses', CoursesViewSet)
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]


