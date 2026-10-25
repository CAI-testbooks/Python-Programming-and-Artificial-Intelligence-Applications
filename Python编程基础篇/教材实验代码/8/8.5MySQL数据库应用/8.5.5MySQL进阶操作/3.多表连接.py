# -*- coding: utf-8 -*-
# 来源：第8章，书内p172；PDF第184页。
# 整理说明：补齐grades、courses、teachers，增加结果输出；实际关联四张表。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    sql = """
    SELECT
        s.name AS student_name,
        c.name AS course_name,
        g.score,
        t.name AS teacher_name
    FROM grades g
    JOIN students s ON g.student_id = s.id
    JOIN courses c ON g.course_id = c.id
    LEFT JOIN teachers t ON c.teacher_id = t.id
    WHERE g.score > 90
    ORDER BY g.score DESC
    """

    with conn.cursor() as cursor:
        cursor.execute(sql)
        top_students = cursor.fetchall()

    print(top_students)
    assert top_students[0]["score"]==95
finally:conn.close()
