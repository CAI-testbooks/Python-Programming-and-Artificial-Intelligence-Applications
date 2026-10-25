# -*- coding: utf-8 -*-
# 来源：第8章，书内p162；PDF第174页。
# 整理说明：为每段补齐独立运行所需的连接、表和演示数据；使用内存库。
import sqlite3

# 连接到SQLite数据库（如果不存在则创建）
conn = sqlite3.connect(':memory:')

# 创建游标对象
cursor = conn.cursor()
print('连接成功')
cursor.close()
conn.close()
