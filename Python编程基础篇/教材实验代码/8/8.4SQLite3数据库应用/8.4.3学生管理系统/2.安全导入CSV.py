# -*- coding: utf-8 -*-
# 来源：第8章，书内p165,166；PDF第177,178页。
from school import *
from pathlib import Path
with closing(init_database()) as conn:
    n=import_from_csv(conn,'majors',Path(__file__).with_name('专业表.csv'))
    assert n==3
    print('成功导入',n,'条专业数据')
