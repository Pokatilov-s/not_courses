from custom_user import models


def get_list_courses_owned_by_author(user: models.User):
    """Получить список курсов принадлежащих автору"""
    # Используя обратную связь course_set получаем все связанные с user объекты из таблицы Courses
    return user.course_set
