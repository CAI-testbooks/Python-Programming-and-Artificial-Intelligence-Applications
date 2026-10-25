# -*- coding: utf-8 -*-
# 来源：第8章，书内p165,166,167；PDF第177,178,179页。
# 整理说明：补齐四张表和转专业日志表；遵循九字段学生结构；修复CSV导入和db_path。
import csv
import sqlite3
from contextlib import closing

def init_database(db_path=':memory:'):
    conn=sqlite3.connect(db_path)
    conn.execute('PRAGMA foreign_keys=ON')
    conn.row_factory=sqlite3.Row
    conn.executescript("\n    CREATE TABLE IF NOT EXISTS majors(major_id TEXT PRIMARY KEY NOT NULL,major_name TEXT NOT NULL);\n    CREATE TABLE IF NOT EXISTS students(\n      student_id TEXT PRIMARY KEY NOT NULL,name TEXT NOT NULL,\n      gender INTEGER NOT NULL DEFAULT 0,birthday TEXT NOT NULL DEFAULT '2000-01-01',\n      major_id TEXT NOT NULL REFERENCES majors(major_id),scholarship NUMERIC,\n      party_member INTEGER,photo BLOB,remark TEXT);\n    CREATE TABLE IF NOT EXISTS courses(course_id TEXT PRIMARY KEY NOT NULL,course_name TEXT NOT NULL,\n      prerequisite TEXT REFERENCES courses(course_id),hours INTEGER NOT NULL,credits INTEGER NOT NULL);\n    CREATE TABLE IF NOT EXISTS grades(student_id TEXT REFERENCES students(student_id),\n      course_id TEXT REFERENCES courses(course_id),score INTEGER NOT NULL,\n      PRIMARY KEY(student_id,course_id));\n    CREATE TABLE IF NOT EXISTS major_changes(student_id TEXT REFERENCES students(student_id),\n      major_id TEXT REFERENCES majors(major_id),changed_at TEXT NOT NULL);\n    ")
    return conn

def seed(conn):
    with conn:
        conn.executemany('INSERT INTO majors VALUES (?,?)',[('M1','计算机科学与技术'),('M2','电子信息工程'),('M3','工商管理')])
        conn.executemany('INSERT INTO students(student_id,name,major_id) VALUES (?,?,?)',
                         [('S1','张三','M1'),('S2','李四','M1'),('S3','王五','M2')])
        conn.execute("INSERT INTO courses VALUES ('C1','Python',NULL,48,3)")
        conn.executemany('INSERT INTO grades VALUES (?,?,?)',[('S1','C1',95),('S2','C1',88)])

def import_from_csv(conn,table,csv_path):
    allowed={'majors','students','courses','grades'}
    if table not in allowed:raise ValueError('未知表名')
    with open(csv_path,encoding='utf-8-sig',newline='') as f:
        reader=csv.reader(f);headers=next(reader)
        columns={row[1] for row in conn.execute('PRAGMA table_info('+table+')')}
        if not headers or len(set(headers))!=len(headers) or not set(headers)<=columns:
            raise ValueError('CSV表头与数据表不匹配')
        sql='INSERT INTO '+table+' ('+','.join('"'+h+'"' for h in headers)+') VALUES ('+','.join('?' for _ in headers)+')'
        with conn:
            with closing(conn.cursor()) as cur:
                cur.executemany(sql,reader)
                return cur.rowcount

class StudentManager:
    def __init__(self,db_path=':memory:'):
        self.conn=init_database(db_path)
    def add_student(self,student_id,name,major_id):
        try:
            with self.conn:
                self.conn.execute('INSERT INTO students(student_id,name,major_id) VALUES (?,?,?)',
                                  (student_id,name,major_id))
        except sqlite3.IntegrityError as e:
            raise ValueError('添加失败（学号、专业或必填字段不合法）：'+str(e)) from e
    def get_top_students(self,course_id,limit=10):
        if not isinstance(limit,int) or limit<=0:raise ValueError('limit必须为正整数')
        return [dict(r) for r in self.conn.execute('\n          SELECT s.student_id,s.name,g.score FROM grades g\n          JOIN students s ON g.student_id=s.student_id WHERE g.course_id=?\n          ORDER BY g.score DESC,s.student_id LIMIT ?',(course_id,limit))]
    def close(self):self.conn.close()

def change_major(conn,student_id,new_major):
    with conn:
        cur=conn.execute('UPDATE students SET major_id=? WHERE student_id=?',(new_major,student_id))
        if cur.rowcount!=1:raise ValueError('学号不存在')
        conn.execute("INSERT INTO major_changes VALUES (?,?,datetime('now'))",(student_id,new_major))

if __name__=='__main__':
    with closing(init_database()) as conn:
        seed(conn)
        print('数据库初始化成功，学生人数：',conn.execute('SELECT COUNT(*) FROM students').fetchone()[0])
