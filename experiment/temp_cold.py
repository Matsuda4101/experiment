import os
import random

def cold_choice(up,down,outer,sl):

    DIR = "photo_storage"
    c_num = []
    c = 0

    a = os.path.join(DIR,up[random.randint(0,(len(up)-1))])         # 上
    if sl != 1:
        c_num.append(a)

    b = os.path.join(DIR,down[random.randint(0,(len(down)-1))])     # 下
    if sl != 2:
        c_num.append(b)
    
    if sl != 3:
        if len(outer) != 0:
            c = os.path.join(DIR,outer[random.randint(0,(len(outer)-1))])   # 上着
            c_num.append(c)
    
    return c_num, a, b, c