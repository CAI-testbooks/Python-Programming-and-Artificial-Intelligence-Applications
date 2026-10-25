# -*- coding: utf-8 -*-
# 来源：第8章，书内p166；PDF第178页。
# 整理说明：补齐tabulate导入和演示数据；人数随数据变化。
from school import *
from tabulate import tabulate
conn=init_database()
seed(conn)
with closing(conn.cursor()) as cur:
    cur.execute("""
        SELECT m.major_name, COUNT(s.student_id) AS total
        FROM majors m
        LEFT JOIN students s ON m.major_id = s.major_id
        GROUP BY m.major_id
    """)
    results = cur.fetchall()
    print(tabulate(results, headers=["专业", "学生人数"]))
conn.close()
