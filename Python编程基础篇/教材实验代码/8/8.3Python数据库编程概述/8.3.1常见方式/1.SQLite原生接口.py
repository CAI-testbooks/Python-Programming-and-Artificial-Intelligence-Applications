# -*- coding: utf-8 -*-
# 来源：第8章，书内p160；PDF第172页。
# SQLite3原生接口示例
import sqlite3
conn = sqlite3.connect('example.db')
print('连接成功')
conn.close()
