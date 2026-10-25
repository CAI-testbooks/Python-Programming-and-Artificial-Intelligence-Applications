# -*- coding: utf-8 -*-
# 来源：第8章，书内p160,161；PDF第172,173页。
# 整理说明：统一使用PyMySQL驱动；异常类取自模块，占位符使用%s。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'8.5MySQL数据库应用'))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    cursor=conn.cursor()
    try:
        cursor.execute('INSERT INTO logs(message) VALUES (%s)',(None,))
    except pymysql.DatabaseError as e:
        print('预期数据库异常：',e);conn.rollback()
    finally:cursor.close()
finally:conn.close()
