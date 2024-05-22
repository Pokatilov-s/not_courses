from django.urls import path
from .views import *

urlpatterns = [
    path('', index_store, name='index_store'),
    path('<uuid:course_uuid>/', course_detail, name='course_detail'),
    path('payment/', payment_page, name='payment_page'),
    path('process_payment/', process_payment, name='process_payment'),
    path('success/', success_page, name='success_page'),
]
