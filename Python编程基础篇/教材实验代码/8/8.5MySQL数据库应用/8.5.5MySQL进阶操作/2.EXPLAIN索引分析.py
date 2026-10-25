# -*- coding: utf-8 -*-
# 来源：第8章，书内p171,172；PDF第183,184页。
# 整理说明：补建idx_name；优化器仍可能按数据量选择全表扫描，不固定断言key。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    with conn.cursor() as cursor:
        cursor.execute("EXPLAIN SELECT * FROM students WHERE name LIKE 'A%'")
        explain_result = cursor.fetchall()
        # 输出结果中的key字段显示使用的索引
        print(explain_result[0]['key'])         # 应输出idx_name

finally:conn.close()
