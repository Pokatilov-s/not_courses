from rest_framework import routers
from django.urls import path, include
from .views import CoursesReadOnlyViewSet, CategoriesViewSet, AddCourseToUser

router = routers.DefaultRouter()
router.register(r'courses', CoursesReadOnlyViewSet, basename='courses')
router.register(r'categories', CategoriesViewSet)
# router.register(r'addcourse', AddCourseToUser)

urlpatterns = [
    path('', include(router.urls)),
    path('addcourse/', AddCourseToUser.as_view(), name='add-course'),
]
