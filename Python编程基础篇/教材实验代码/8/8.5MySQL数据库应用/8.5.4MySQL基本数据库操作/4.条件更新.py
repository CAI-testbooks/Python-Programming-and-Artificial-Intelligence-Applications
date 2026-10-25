# -*- coding: utf-8 -*-
# 来源：第8章，书内p170；PDF第182页。
# 整理说明：补齐专用练习库建表、数据和公共连接。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    update_sql = """
    UPDATE students
    SET gpa = %s
    WHERE id = %s AND gpa IS NOT NULL
    """

    affected = safe_execute(conn,update_sql, (3.9, 101))
    print(f"更新了 {affected} 条记录")

    assert affected==1
finally:conn.close()
