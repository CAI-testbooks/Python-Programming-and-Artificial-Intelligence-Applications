# -*- coding: utf-8 -*-
# 来源：第8章，书内p169；PDF第181页。
# 整理说明：补齐专用练习库建表、数据和公共连接。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    with conn.cursor() as cursor:
        cursor.execute('SHOW CREATE TABLE students')
        print(cursor.fetchone())
finally:conn.close()
