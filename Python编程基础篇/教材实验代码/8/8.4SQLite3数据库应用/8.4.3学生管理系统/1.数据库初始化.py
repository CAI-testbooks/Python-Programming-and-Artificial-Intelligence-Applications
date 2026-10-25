# -*- coding: utf-8 -*-
# 来源：第8章，书内p165；PDF第177页。
from school import *
with closing(init_database()) as conn:
    seed(conn)
    print([r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")])
