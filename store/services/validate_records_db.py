from store.models import UserCourse


def check_user_enrollment(user_uuid, course_uuid):
    """Проверить регистрацию пользователя на курс"""
    return UserCourse.objects.is_enrolled(user_uuid=user_uuid, course_uuid=course_uuid)
