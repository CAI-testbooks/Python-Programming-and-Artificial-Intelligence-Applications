# -*- coding: utf-8 -*-
# 来源：第8章，书内p159；PDF第171页。
# 整理说明：将SQL语句放入sqlite3执行器；补充表和数据。
import sqlite3
conn=sqlite3.connect(':memory:')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Students (\n    StudentID INT PRIMARY KEY,  -- 学生ID，主键\n    Name VARCHAR(50),           -- 学生姓名\n    Age INT,                    -- 学生年龄\n    Major VARCHAR(50)           -- 学生专业\n);\n')
cursor.execute('ALTER TABLE Students\nADD COLUMN Email VARCHAR(100);  -- 添加Email列\n')
cursor.execute("INSERT INTO Students (StudentID, Name, Age, Major, Email)\nVALUES (1, '张三', 20, '计算机科学', 'zhangsan@example.com');\n")
cursor.execute('SELECT * FROM Students;\n')
print('执行：SELECT * FROM Students;', cursor.fetchall())
cursor.execute("SELECT Name, Age FROM Students\nWHERE Major = '计算机科学';\n")
print('执行：SELECT Name, Age FROM Students', cursor.fetchall())
cursor.execute('SELECT * FROM Students\nORDER BY Age ASC;\n')
print('执行：SELECT * FROM Students', cursor.fetchall())
conn.commit()
conn.close()
