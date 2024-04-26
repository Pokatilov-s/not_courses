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
        fields = ('uuid', 'course_uuid', 'status', 'user_uuid')
        read_only_fields = ('uuid', 'user_uuid')

    def create(self, validated_data):
        # Вытаскиваем пользователя из контекста запроса
        user = self.context['request'].user
        validated_data['user_uuid'] = user
        course = validated_data.get('course_uuid')
        # Проверка уникальности записи
        if UserCourse.objects.filter(user_uuid=user, course_uuid=course).exists():
            error_message = {
                "non field errors": {
                    "message": 'The user is already enrolled in a course.',
                    "details": {
                        "user_uuid": user.uuid,
                        "course_uuid": course.uuid
                    }
                 }
            }
            raise serializers.ValidationError(error_message)
            # raise serializers.ValidationError("This user is already enrolled in this course.")

        return super().create(validated_data)
