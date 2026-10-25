# -*- coding: utf-8 -*-
# 来源：第8章，书内p168,169,171；PDF第180,181,183页。
# 整理说明：连接参数来自环境变量；补齐依赖表、字段和演示数据；修复转账检查。
import os
import pymysql

def connect():
    kwargs=dict(host=os.getenv('BOOK_MYSQL_HOST','127.0.0.1'),
      port=int(os.getenv('BOOK_MYSQL_PORT','3306')),user=os.getenv('BOOK_MYSQL_USER','root'),
      password=os.getenv('BOOK_MYSQL_PASSWORD',''),database=os.getenv('BOOK_MYSQL_DATABASE','book_ch08_demo'),
      charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,connect_timeout=5)
    ca=os.getenv('BOOK_MYSQL_SSL_CA')
    if ca:kwargs['ssl']={'ca':ca}
    return pymysql.connect(**kwargs)

def setup(conn):
    # 仅在专用练习库重置数据，禁止指向生产数据库。
    if not conn.db.decode().startswith('book_ch08_'):raise ValueError('请使用book_ch08_开头的专用练习库')
    with conn.cursor() as c:
        c.execute('SET FOREIGN_KEY_CHECKS=0')
        for t in ['transaction_log','accounts','logs','users','grades','courses','teachers','students','majors']:
            c.execute('DROP TABLE IF EXISTS '+t)
        c.execute('SET FOREIGN_KEY_CHECKS=1')
        statements=[
          'CREATE TABLE majors(id INT PRIMARY KEY,name VARCHAR(50)) ENGINE=InnoDB',
          'CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50) NOT NULL,gpa DECIMAL(3,2) CHECK(gpa BETWEEN 0 AND 4),major_id INT,INDEX idx_major(major_id),INDEX idx_name(name),is_deleted TINYINT DEFAULT 0,deleted_at DATETIME,FOREIGN KEY(major_id) REFERENCES majors(id)) ENGINE=InnoDB',
          'CREATE TABLE teachers(id INT PRIMARY KEY,name VARCHAR(50)) ENGINE=InnoDB',
          'CREATE TABLE courses(id INT PRIMARY KEY,name VARCHAR(50),teacher_id INT,FOREIGN KEY(teacher_id) REFERENCES teachers(id)) ENGINE=InnoDB',
          'CREATE TABLE grades(student_id INT,course_id INT,score INT,PRIMARY KEY(student_id,course_id),FOREIGN KEY(student_id) REFERENCES students(id),FOREIGN KEY(course_id) REFERENCES courses(id)) ENGINE=InnoDB',
          'CREATE TABLE accounts(id INT PRIMARY KEY,balance DECIMAL(12,2) NOT NULL) ENGINE=InnoDB',
          'CREATE TABLE transaction_log(id INT AUTO_INCREMENT PRIMARY KEY,from_acc INT,to_acc INT,amount DECIMAL(12,2)) ENGINE=InnoDB',
          'CREATE TABLE users(id INT PRIMARY KEY,name VARCHAR(50),age INT) ENGINE=InnoDB',
          'CREATE TABLE logs(message VARCHAR(100) NOT NULL) ENGINE=InnoDB']
        for sql in statements:c.execute(sql)
        c.executemany('INSERT INTO majors VALUES (%s,%s)',[(1,'计算机'),(2,'电子信息'),(3,'工商管理')])
        c.executemany('INSERT INTO students(id,name,gpa,major_id) VALUES (%s,%s,%s,%s)',[(101,'Alice',3.8,1),(205,'Bob',3.5,2)])
        c.execute("INSERT INTO teachers VALUES (1,'王老师')")
        c.execute("INSERT INTO courses VALUES (1,'Python',1)")
        c.execute('INSERT INTO grades VALUES (101,1,95)')
        c.executemany('INSERT INTO accounts VALUES (%s,%s)',[(1,100),(2,50)])
        c.execute("INSERT INTO users VALUES (1,'Alice',20)")
    conn.commit()

def safe_execute(conn,sql,params=None):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql,params or ())
            count=cursor.rowcount
        conn.commit()
        return count
    except pymysql.Error:
        conn.rollback()
        raise

def transfer_funds(conn,from_acc,to_acc,amount):
    from decimal import Decimal
    amount=Decimal(str(amount))
    if not amount.is_finite() or amount<=0 or from_acc==to_acc:
        raise ValueError('转账金额必须大于0且账户不同')
    try:
        conn.begin()
        with conn.cursor() as c:
            c.execute('UPDATE accounts SET balance=balance-%s WHERE id=%s AND balance>=%s',(amount,from_acc,amount))
            if c.rowcount!=1:raise ValueError('扣款账户不存在或余额不足')
            c.execute('UPDATE accounts SET balance=balance+%s WHERE id=%s',(amount,to_acc))
            if c.rowcount!=1:raise ValueError('收款账户不存在')
            c.execute('INSERT INTO transaction_log(from_acc,to_acc,amount) VALUES (%s,%s,%s)',(from_acc,to_acc,amount))
        conn.commit()
        return True
    except (pymysql.Error,ValueError):
        conn.rollback()
        raise

if __name__=='__main__':
    conn=connect()
    try:
        setup(conn)
        print('MySQL测试表和数据准备成功')
    finally:conn.close()
