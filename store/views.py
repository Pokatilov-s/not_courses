from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import UserCourse
from custom_user.models import User
from forge.models import Course, Category
from .serializers import ReadOnlyCourseSerializer, ReadOnlyCategorySerializer, UserCourseSerializer


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ReadOnlyCategorySerializer


class CoursesReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.filter(status='published')
    serializer_class = ReadOnlyCourseSerializer


class AddCourseToUser(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = UserCourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


class CoursesAddedUser(ListAPIView):
    serializer_class = ReadOnlyCourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_uuid = self.request.user.uuid
        print(user_uuid)
        queryset = UserCourse.objects.filter(user_uuid=user_uuid)
        print(queryset)
        user = User.objects.get(uuid=user_uuid)
        courses = user.usercourse_set.filter(user_uuid='user_uuid')
        print(courses)
        # queryset = Course.objects.filter(usercourses=user_uuid )
        # print(queryset)
        # return queryset
        # user_with_courses = get_object_or_404(User, uuid=user.uuid)
        # print(user_with_courses.usercourse_set.all())
        # # return user_with_courses.usercourse_set.all()
        # print(get_object_or_404(UserCourse, user_uuid=user.uuid).course.all())

