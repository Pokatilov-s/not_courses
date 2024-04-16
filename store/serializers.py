from rest_framework import serializers
from forge.models import Course, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'updated_at')
        read_only_fields = ('id', 'title', 'updated_at')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('uuid', 'category', 'title', 'price', 'description', 'status', 'author_uuid', 'updated_at',
                  'students_qty', 'reviews_qty')
        read_only_fields = ('uuid', 'category', 'title', 'price', 'description', 'status', 'author_uuid',
                            'updated_at', 'students_qty', 'reviews_qty')
