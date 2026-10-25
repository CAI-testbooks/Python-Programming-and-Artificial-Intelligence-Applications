# -*- coding: utf-8 -*-
# 来源：第8章，书内p169,170；PDF第181,182页。
# 整理说明：补齐专用练习库建表、数据和公共连接。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    students = [
        ('Alice', 3.8, 1),
        ('Bob', 3.5, 2),
        ('Charlie', None, 3)  # 允许NULL
    ]

    with conn.cursor() as cursor:
        cursor.executemany(
            "INSERT INTO students (name, gpa, major_id) VALUES (%s, %s, %s)",
            students
        )
        conn.commit()
        print(f"插入 {cursor.rowcount} 条记录")

finally:conn.close()
