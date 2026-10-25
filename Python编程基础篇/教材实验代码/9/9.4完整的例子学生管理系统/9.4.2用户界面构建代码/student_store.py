# -*- coding: utf-8 -*-
# 来源：第9章，书内p208,209,210,211,212；PDF第220,221,222,223,224页。
# 整理说明：将数据库操作拆出，补齐表结构、演示数据、类型转换和资源释放。
import os,csv,sqlite3
from pathlib import Path
from contextlib import closing

BASE=Path(__file__).resolve().parent
DB_PATH=Path(os.environ.get('BOOK_STUDENT_DB',str(BASE/'student.db')))
def connect_db():
    conn=sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys=ON')
    return conn

def reset_database():
    # 配套数据为本次整理自建的演示数据，不是教材原始素材。
    with (BASE/'学生表.txt').open(encoding='gbk',newline='') as f:
        rows=list(csv.reader(f))
    with closing(connect_db()) as conn:
        with conn:
            conn.execute('BEGIN')
            conn.execute('DROP TABLE IF EXISTS 成绩表')
            conn.execute('DROP TABLE IF EXISTS 学生表')
            conn.execute('DROP TABLE IF EXISTS 课程表')
            conn.execute('DROP TABLE IF EXISTS 专业表')
            conn.execute('CREATE TABLE 专业表(专业编号 TEXT PRIMARY KEY NOT NULL,专业名称 TEXT NOT NULL)')
            conn.executemany('INSERT INTO 专业表 VALUES (?,?)',[('M1','计算机科学与技术'),('M2','电子信息工程'),('M3','工商管理')])
            conn.execute('CREATE TABLE 学生表(\n              学号 TEXT PRIMARY KEY NOT NULL,姓名 TEXT NOT NULL,\n              性别 INTEGER NOT NULL CHECK(性别 IN(0,1)),生日 TEXT NOT NULL,\n              专业编号 TEXT NOT NULL REFERENCES 专业表(专业编号) ON UPDATE CASCADE,\n              奖学金 NUMERIC,党员 INTEGER CHECK(党员 IN(0,1)),照片 BLOB,备注 TEXT)')
            conn.execute('CREATE TABLE 课程表(课程号 TEXT PRIMARY KEY,课程名称 TEXT,先修课程代码 TEXT,学时 INTEGER,学分 INTEGER)')
            conn.execute('CREATE TABLE 成绩表(学号 TEXT REFERENCES 学生表(学号) ON DELETE CASCADE,课程号 TEXT REFERENCES 课程表(课程号),成绩 INTEGER,PRIMARY KEY(学号,课程号))')
            for r in rows:
                if len(r)!=9:raise ValueError('演示数据必须为9列')
                r[2]=int(r[2]);r[5]=float(r[5]) if r[5] else None
                r[6]=int(r[6]) if r[6] else None;r[7]=None
                conn.execute('INSERT INTO 学生表 VALUES (?,?,?,?,?,?,?,?,?)',r)

def add_student(info):
    from datetime import date
    from decimal import Decimal, InvalidOperation
    if not all(info[k].strip() for k in ['学号','姓名','生日','专业编号']):
        raise ValueError('学号、姓名、生日、专业编号不能为空')
    if info['性别'] not in ['男','女']:raise ValueError('性别必须是男或女')
    try:date.fromisoformat(info['生日'])
    except ValueError:raise ValueError('生日格式必须为YYYY-MM-DD且日期有效')
    scholarship=None
    if info['奖学金']:
        try:
            value=Decimal(info['奖学金'])
            if not value.is_finite() or value<0:raise ValueError()
            scholarship=float(value)
        except (ValueError,InvalidOperation):raise ValueError('奖学金必须为非负数字')
    if info['党员'] not in ['', '0','1']:raise ValueError('党员必须是0或1')
    values=(info['学号'].strip(),info['姓名'].strip(),1 if info['性别']=='男' else 0,
      info['生日'],info['专业编号'].strip(),scholarship,
      int(info['党员']) if info['党员'] else None,None,info['备注'])
    with closing(connect_db()) as conn:
        with conn:conn.execute('INSERT INTO 学生表 VALUES (?,?,?,?,?,?,?,?,?)',values)

def delete_student(student_id):
    with closing(connect_db()) as conn:
        with conn:
            return conn.execute('DELETE FROM 学生表 WHERE 学号=?',(student_id,)).rowcount==1

def query_students(limit):
    if not isinstance(limit,int) or limit<=0:raise ValueError('请输入一个正整数')
    with closing(connect_db()) as conn:
        return conn.execute('SELECT * FROM 学生表 ORDER BY 学号 LIMIT ?',(limit,)).fetchall()

if __name__=='__main__':
    # 直接运行只检查连接，不执行重置。
    with closing(connect_db()) as conn:print('数据库连接成功：',DB_PATH)
