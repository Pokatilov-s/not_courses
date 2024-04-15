import uuid
from django.db import models

from custom_user.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'


class Course(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True)
    students_qty = models.IntegerField(default=0)
    reviews_qty = models.IntegerField(default=0)
    author_uuid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='author_uuid')
    status = models.CharField(max_length=20, default="draft")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'courses'


class UserCourse(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_uuid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_uuid')
    course_uuid = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_uuid')
    status = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'user_courses'
