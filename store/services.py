from django.db.models.query import QuerySet
from forge.models import Course, Category
from django.db import connection
from collections import namedtuple
from typing import List, Tuple


def get_list_published_courses() -> QuerySet[Course]:
    return Course.objects.filter(status='published')


def get_list_categories() -> QuerySet[Category]:
    return Category.objects.all()


def get_list_courses_added_to_user(user_uuid: str) -> List[Tuple]:
    def named_tuple_fetchall(cursors):
        # "Return all rows from a cursor as a namedtuple"
        desc = cursors.description
        nt_result = namedtuple('Course', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.* FROM user_courses us
            LEFT JOIN courses c
            ON c.uuid = us.course_uuid
            WHERE user_uuid = %s""", [user_uuid])
        rows = named_tuple_fetchall(cursor)
        print(rows)
        return rows
