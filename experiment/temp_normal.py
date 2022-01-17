import os
import random

def normal_choice(up,down,outer,sl):

    DIR = "photo_storage"
    c_num = []
    c = 0

    up_choice = up[random.randint(0,(len(up)-1))]
    a = os.path.join(DIR,up_choice)         # 上
    if sl != 1:
        c_num.append(a)

    b = os.path.join(DIR,down[random.randint(0,(len(down)-1))])     # 下
    if sl != 2:
        c_num.append(b)

    if sl != 1:
        if len(outer) != 0:

            if up_choice == "Tshirt_LS":
                c = os.path.join(DIR,outer[random.randint(0,(len(outer)-1))])   # 上着
                c_num.append(c)
    
    return c_num, a, b, c