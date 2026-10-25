# -*- coding: utf-8 -*-
# 来源：第8章，书内p169；PDF第181页。
# 整理说明：保留教材参数化CREATE USER示例；需要管理员权限，仅创建并清理临时演示账户。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    with conn.cursor() as cursor:
        cursor.execute('CREATE USER %s@%s IDENTIFIED BY %s',('book_ch08_web','192.168.1.%','DemoOnly_2026!'))
        print('演示用户创建成功')
        cursor.execute('DROP USER %s@%s',('book_ch08_web','192.168.1.%'))
finally:conn.close()
