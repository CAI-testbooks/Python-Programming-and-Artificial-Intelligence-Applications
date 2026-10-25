# -*- coding: utf-8 -*-
# 来源：第8章，书内p159；PDF第171页。
# 整理说明：需要演示库管理员权限；创建临时账户验证GRANT和REVOKE，完成后删除该账户。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'8.5MySQL数据库应用'))
from mysql_common import *
conn=connect()

try:
    setup(conn)
    with conn.cursor() as cur:
        cur.execute("CREATE USER IF NOT EXISTS 'book_ch08_reader'@'localhost' IDENTIFIED BY 'DemoOnly_2026!'")
        cur.execute("GRANT SELECT ON book_ch08_demo.students TO 'book_ch08_reader'@'localhost'")
        cur.execute("SHOW GRANTS FOR 'book_ch08_reader'@'localhost'")
        grants=cur.fetchall();print('授予后：',grants)
        assert any('SELECT' in str(r) for r in grants)
        cur.execute("REVOKE SELECT ON book_ch08_demo.students FROM 'book_ch08_reader'@'localhost'")
        cur.execute("SHOW GRANTS FOR 'book_ch08_reader'@'localhost'")
        grants=cur.fetchall();print('撤销后：',grants)
        assert not any('SELECT' in str(r) for r in grants)
        cur.execute("DROP USER 'book_ch08_reader'@'localhost'")
finally:conn.close()
