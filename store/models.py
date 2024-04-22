import uuid
from django.db import models
from forge.models import Course
from custom_user.models import User


class UserCourse(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_uuid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_uuid')
    course_uuid = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_uuid')
    status = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'user_courses'
        unique_together = ('user_uuid', 'course_uuid')
        indexes = [
            models.Index(fields=['user_uuid'])
        ]
