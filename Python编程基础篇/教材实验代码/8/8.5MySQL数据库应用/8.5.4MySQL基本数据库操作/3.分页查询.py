# -*- coding: utf-8 -*-
# 来源：第8章，书内p170；PDF第182页。
# 整理说明：保留分页函数，增加实际调用和输出；教材3条数据查询第2页可能为空。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    def query_students(page=1, page_size=10):
        offset = (page - 1) * page_size
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.id, s.name, m.name AS major, s.gpa
                FROM students s
                JOIN majors m ON s.major_id = m.id
                ORDER BY s.id
                LIMIT %s OFFSET %s
            """, (page_size, offset))
            return cursor.fetchall()

    # 使用示例
    page2_data = query_students(page=2)

    print(query_students(page=1,page_size=1))
    assert len(query_students(page=1,page_size=1))==1

finally:conn.close()
