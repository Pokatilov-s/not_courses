from rest_framework import serializers
from forge.models import Course, Category
from .models import UserCourse


class ReadOnlyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'updated_at')
        read_only_fields = ('id', 'title', 'updated_at')


class ReadOnlyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('uuid', 'category', 'title', 'price', 'description', 'status', 'author_uuid', 'updated_at',
                  'students_qty', 'reviews_qty')
        read_only_fields = ('uuid', 'category', 'title', 'price', 'description', 'status', 'author_uuid',
                            'updated_at', 'students_qty', 'reviews_qty')


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'
