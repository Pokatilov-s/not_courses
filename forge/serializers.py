from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('uuid', 'category', 'title', 'price', 'description', 'status', 'author_uuid', 'updated_at',
                  'students_qty', 'reviews_qty')
        read_only_fields = ('updated_at', 'status', 'students_qty', 'reviews_qty', 'author_uuid')
