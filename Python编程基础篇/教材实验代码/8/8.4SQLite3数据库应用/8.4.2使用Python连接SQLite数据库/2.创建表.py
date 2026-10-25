# -*- coding: utf-8 -*-
# 来源：第8章，书内p162；PDF第174页。
# 整理说明：为每段补齐独立运行所需的连接、表和演示数据；使用内存库。
import sqlite3
conn=sqlite3.connect(':memory:')
cursor=conn.cursor()
# 创建Students表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Major TEXT
)
''')

# 提交更改
conn.commit()
print(cursor.execute("PRAGMA table_info(Students)").fetchall())
cursor.close()
conn.close()
