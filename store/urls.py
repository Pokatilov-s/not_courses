from rest_framework import routers
from django.urls import path, include
from .views import CoursesReadOnlyViewSet, CategoriesViewSet, AddCourseToUser, CoursesAddedUser
from store.payment.view import *
from store.payment.test_pay_notific import payment_webhook

router = routers.SimpleRouter()
router.register(r'courses', CoursesReadOnlyViewSet, basename='courses')
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_course/', AddCourseToUser.as_view(), name='add-course'),
    path('my_course/', CoursesAddedUser.as_view(), name='my-course'),
    # Платёжка
    path('pay_page/', payment_page, name='payment_page'),
    path('process_payment/', process_payment, name='process_payment'),
    path('success/', success_page, name='success_page'),
    # Тест уведомлений оплаты
    path('payment_webhook/', payment_webhook)
]

