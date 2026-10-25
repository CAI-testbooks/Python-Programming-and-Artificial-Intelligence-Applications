# -*- coding: utf-8 -*-
# 来源：第8章，书内p160；PDF第172页。
# 整理说明：统一使用PyMySQL驱动；异常类取自模块，占位符使用%s。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'8.5MySQL数据库应用'))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    with conn.cursor() as c:
        c.execute('SELECT VERSION() AS version');print(c.fetchone())
finally:conn.close()
