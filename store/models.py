import uuid
from django.db import models
from forge.models import Course
from custom_user.models import User


class TransactionsDetails(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bank = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'transactions_details'


class UserCourse(models.Model):
    class Status(models.TextChoices):
        PROCESSING = 'processing', 'Processing'
        SUCCESS = 'success', 'Success'
        ERROR = 'error', 'Error'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_uuid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_uuid')
    course_uuid = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_uuid')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PROCESSING)
    transaction_uuid = models.ForeignKey(TransactionsDetails, db_column='transaction_uuid', on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'user_courses'
        unique_together = ('user_uuid', 'course_uuid')
        indexes = [
            models.Index(fields=['user_uuid'])
        ]
