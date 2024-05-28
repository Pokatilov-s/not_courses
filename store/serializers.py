from rest_framework import serializers
from forge.models import Course, Category
from .models import UserCourse, TransactionsDetails
from .services.validate_records_db import check_user_enrollment


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
        fields = ('course_uuid', 'status', 'user_uuid', 'transaction_uuid')
        read_only_fields = ('uuid',)


class CoursesAddedUserSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    category_id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    description = serializers.CharField()
    students_qty = serializers.IntegerField()
    reviews_qty = serializers.IntegerField()
    author_uuid = serializers.UUIDField()
    status = serializers.CharField()
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()


class TransactionsDetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsDetails
        fields = ('course_uuid', 'price', 'bank',)
