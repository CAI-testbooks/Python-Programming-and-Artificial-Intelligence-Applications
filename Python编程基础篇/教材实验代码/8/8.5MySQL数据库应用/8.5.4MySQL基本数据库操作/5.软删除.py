# -*- coding: utf-8 -*-
# 来源：第8章，书内p170；PDF第182页。
# 整理说明：补齐is_deleted和deleted_at字段。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    # 实际生产环境推荐添加is_deleted字段标记
    safe_execute(conn,"""
        UPDATE students
        SET is_deleted = 1, deleted_at = NOW()
        WHERE id = %s
    """, (205,))

    with conn.cursor() as c:
        c.execute('SELECT is_deleted,deleted_at FROM students WHERE id=205')
        row=c.fetchone();print(row);assert row['is_deleted']==1 and row['deleted_at'] is not None
finally:conn.close()
