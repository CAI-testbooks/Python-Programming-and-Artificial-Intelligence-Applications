# -*- coding: utf-8 -*-
# 来源：第8章，书内p169；PDF第181页。
# 整理说明：演示普通数据写入；创建用户属于管理员操作，另附SQL。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    print(safe_execute(conn,"INSERT INTO logs(message) VALUES (%s)",('测试日志',)))
finally:conn.close()
