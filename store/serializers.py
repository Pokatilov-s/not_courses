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
        fields = ('uuid', 'user_uuid', 'course_uuid', 'status')
        # read_only_fields = ('uuid', 'user_uuid')

    # def create(self, validated_data):
    #     # Получаем пользователя из контекста запроса
    #     user = self.context['request'].user
    #
    #     # Выводим все атрибуты запроса
    #     print(user.uuid, user.username)
    #
    #     # Добавляем пользователя к данным перед сохранением
    #     validated_data['user_uuid'] = user
    #     # Вызываем метод create базового класса для сохранения данных
    #     return super().create(validated_data)
