# -*- coding: utf-8 -*-
# 来源：第8章，书内p163；PDF第175页。
# 整理说明：为每段补齐独立运行所需的连接、表和演示数据；使用内存库。
import sqlite3
conn=sqlite3.connect(':memory:')
cursor=conn.cursor()
# 关闭游标和连接
cursor.close()
conn.close()
