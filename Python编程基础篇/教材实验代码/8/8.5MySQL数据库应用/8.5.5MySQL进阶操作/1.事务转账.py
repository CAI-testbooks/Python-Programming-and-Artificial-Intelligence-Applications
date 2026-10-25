# -*- coding: utf-8 -*-
# 来源：第8章，书内p171；PDF第183页。
# 整理说明：检查扣款与收款的rowcount，失败时回滚；验证余额不足和收款人不存在。
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mysql_common import *
conn=connect()
try:
    setup(conn)
    assert transfer_funds(conn,1,2,30)
    for args in [(1,2,1000),(1,999,10)]:
        try:transfer_funds(conn,*args)
        except ValueError as e:print('预期拒绝：',e)
        else:raise AssertionError('应拒绝无效转账')
    with conn.cursor() as c:
        c.execute('SELECT * FROM accounts ORDER BY id');rows=c.fetchall();print(rows)
        assert [float(r['balance']) for r in rows]==[70.0,80.0]
        c.execute('SELECT COUNT(*) AS n FROM transaction_log');assert c.fetchone()['n']==1
finally:conn.close()
