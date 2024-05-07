def get_list_courses_owned_by_author(user, status=None):
    """Получить список курсов принадлежащих автору"""
    # Используя обратную связь course_set получаем все связанные с user объекты из таблицы Courses
    # если передаётся status фильтруем по статусу
    if status is not None:
        return user.course_set.filter(status=status)

    return user.course_set
