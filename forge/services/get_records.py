from rest_framework.generics import get_object_or_404


def get_list_courses_owned_by_author(user):
    """Получить список курсов принадлежащих автору"""
    # Используя обратную связь course_set получаем все связанные с user объекты из таблицы Courses
    return user.course_set


def get_courses_owned_by_author(user, pk):
    """Получить экземпляр курса принадлежащий автору"""
    return get_object_or_404(user.course_set, pk=pk)
