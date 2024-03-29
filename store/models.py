import uuid
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Courses(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True)
    students_qty = models.IntegerField(default=0)
    reviews_qty = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class ImagesPreview(models.Model):
#     curse_uuid = models.OneToOneField(Courses, on_delete=models.CASCADE, primary_key=True)
#     image = models.ImageField(upload_to='')
