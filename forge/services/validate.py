from forge.models import Course


def check_existence_this_course(**kwargs):
    """Проверить существование курса"""
    return Course.objects.is_exists(**kwargs)
