from rest_framework import routers
from django.urls import path, include
from .views import CoursesReadOnlyViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'courses', CoursesReadOnlyViewSet)
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
