from django.db import models


class CourseManager(models.Manager):
    def is_exists(self, **kwargs):
        """Проверить существование записи о курсе"""
        return self.filter(**kwargs).exists()
