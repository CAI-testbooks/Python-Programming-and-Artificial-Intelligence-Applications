# -*- coding: utf-8 -*-
# 来源：第8章，书内p169；PDF第181页。
-- 需要CREATE USER权限；不要由普通应用账户执行。
CREATE USER IF NOT EXISTS 'book_ch08_web'@'192.168.1.%' IDENTIFIED BY 'DemoOnly_2026!';
