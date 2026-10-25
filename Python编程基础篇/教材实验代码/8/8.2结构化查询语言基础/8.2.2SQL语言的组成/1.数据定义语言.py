# -*- coding: utf-8 -*-
# 来源：第8章，书内p158；PDF第170页。
# 整理说明：将SQL语句放入sqlite3执行器；补充表和数据。
import sqlite3
conn=sqlite3.connect(':memory:')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Students (\n    StudentID INT PRIMARY KEY,  -- 学生ID，主键\n    Name VARCHAR(50),           -- 学生姓名\n    Age INT,                    -- 学生年龄\n    Major VARCHAR(50)           -- 学生专业\n);\n')
print('执行：CREATE TABLE IF NOT EXISTS Students (', cursor.fetchall())
cursor.execute('ALTER TABLE Students\nADD COLUMN Email VARCHAR(100);  -- 添加Email列\n')
print('执行：ALTER TABLE Students', cursor.fetchall())
cursor.execute('DROP TABLE Students;  -- 删除表\n')
print('执行：DROP TABLE Students;  -- 删除表', cursor.fetchall())
conn.commit()
conn.close()
