from django.db import models


class UserCourseManager(models.Manager):
    def is_enrolled(self, user_uuid, course_uuid):
        """Проверить наличие связи user и course"""
        return self.filter(user_uuid=user_uuid, course_uuid=course_uuid).exists()
