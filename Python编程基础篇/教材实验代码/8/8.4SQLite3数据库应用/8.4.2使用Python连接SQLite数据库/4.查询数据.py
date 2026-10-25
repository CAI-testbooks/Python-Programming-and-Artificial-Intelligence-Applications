# -*- coding: utf-8 -*-
# 来源：第8章，书内p163；PDF第175页。
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
# 插入数据
cursor.execute("""
INSERT INTO Students (StudentID, Name, Age, Major)
VALUES (1, '张三', 20, '计算机科学')
""")

# 提交更改
conn.commit()
# 查询所有学生信息
cursor.execute("SELECT * FROM Students")
results = cursor.fetchall()

# 打印查询结果
for row in results:
    print(row)
cursor.close()
conn.close()
