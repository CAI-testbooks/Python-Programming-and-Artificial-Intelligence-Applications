# -*- coding: utf-8 -*-
# 来源：第8章，书内p168；PDF第180页。
# 整理说明：补齐专用练习库建表、数据和公共连接。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    # 推荐使用上下文管理器
    with conn.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        print(cursor.fetchone())         # 输出: {'VERSION()': '8.0.32'}

finally:conn.close()
