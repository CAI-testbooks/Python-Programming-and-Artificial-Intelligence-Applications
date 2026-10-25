# -*- coding: utf-8 -*-
# 来源：第8章，书内p167；PDF第179页。
from school import *
with closing(init_database()) as conn:
    seed(conn)
    change_major(conn,'S1','M2')
    assert conn.execute("SELECT major_id FROM students WHERE student_id='S1'").fetchone()[0]=='M2'
    assert conn.execute('SELECT COUNT(*) FROM major_changes').fetchone()[0]==1
    try:change_major(conn,'S1','不存在')
    except sqlite3.IntegrityError:print('无效专业被拒绝，事务回滚')
    assert conn.execute("SELECT major_id FROM students WHERE student_id='S1'").fetchone()[0]=='M2'
    print('转专业和回滚验证通过')
