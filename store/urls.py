from rest_framework import routers
from django.urls import path, include
from .views import CoursesReadOnlyViewSet, CategoriesViewSet, AddCourseToUser, CoursesAddedUser

router = routers.SimpleRouter()
router.register(r'courses', CoursesReadOnlyViewSet, basename='courses')
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_course/', AddCourseToUser.as_view(), name='add-course'),
    path('my_course/', CoursesAddedUser.as_view(), name='my-course'),
]
