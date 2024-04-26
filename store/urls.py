from rest_framework import routers
from django.urls import path, include
from .views import CoursesReadOnlyViewSet, CategoriesViewSet, AddCourseToUser, CoursesAddedUser

router = routers.DefaultRouter()
router.register(r'courses', CoursesReadOnlyViewSet, basename='courses')
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addcourse/', AddCourseToUser.as_view(), name='add-course'),
    path('mycourse/', CoursesAddedUser.as_view(), name='my-course'),
]
