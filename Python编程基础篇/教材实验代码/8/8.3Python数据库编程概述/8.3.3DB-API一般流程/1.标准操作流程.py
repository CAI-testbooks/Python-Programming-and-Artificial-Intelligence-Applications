# -*- coding: utf-8 -*-
# 来源：第8章，书内p161；PDF第173页。
# 整理说明：补充查询输出和显式关闭连接。
import sqlite3

# 1. 建立连接
with sqlite3.connect(':memory:') as conn:
    # 2. 创建游标
    cursor = conn.cursor()

    try:
        # 3. 执行SQL
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

        # 4. 插入数据（参数化查询）
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                      ('Alice', 'alice@example.com'))

        # 5. 提交事务
        conn.commit()

    except sqlite3.Error as e:
        print(f"操作失败: {e}")
        conn.rollback()

    finally:
        # 6. 关闭游标
        cursor.close()
print(conn.execute("SELECT * FROM users").fetchall())
conn.close()
