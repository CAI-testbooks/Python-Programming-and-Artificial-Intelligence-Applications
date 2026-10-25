# -*- coding: utf-8 -*-
# 来源：第8章，书内p166；PDF第178页。
from school import *
m=StudentManager()
try:
    seed(m.conn)
    m.add_student('S4','赵六','M3')
    print(m.get_top_students('C1',2))
    assert m.get_top_students('C1',1)[0]['score']==95
finally:m.close()
