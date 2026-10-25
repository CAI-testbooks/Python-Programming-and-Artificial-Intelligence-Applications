# -*- coding: utf-8 -*-
# 来源：第8章，书内p159；PDF第171页。
-- 先由管理员创建演示账户；只作用于专用练习库。
CREATE USER IF NOT EXISTS 'book_ch08_reader'@'localhost' IDENTIFIED BY 'DemoOnly_2026!';
GRANT SELECT ON book_ch08_demo.students TO 'book_ch08_reader'@'localhost';
REVOKE SELECT ON book_ch08_demo.students FROM 'book_ch08_reader'@'localhost';
