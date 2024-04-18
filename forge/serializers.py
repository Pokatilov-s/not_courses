from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('uuid', 'category', 'title', 'price', 'description', 'status', 'author_uuid', 'updated_at',
                  'students_qty', 'reviews_qty')
        read_only_fields = ('updated_at', 'status', 'students_qty', 'reviews_qty')






# class CourseSerializer(serializers.Serializer):
#     uuid = serializers.UUIDField(read_only=True)
#     category = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     description = serializers.CharField()
#     status = serializers.ChoiceField(choices=Course.Status)
#     author_uuid = serializers.UUIDField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     students_qty = serializers.IntegerField(read_only=True)
#     reviews_qty = serializers.IntegerField(read_only=True)
#
#     def create(self, validated_data):
#         return Course.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.category = validated_data.get('category', instance.category)
#         instance.title = validated_data.get('title', instance.title)
#         instance.price = validated_data.get('price', instance.price)
#         instance.description = validated_data.get('description', instance.description)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance

