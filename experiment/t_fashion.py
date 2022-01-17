# 夏の服画像取得
import random
import os

DIR = "make_model_photo"

def tekitou():
    up = ["poloshirt","Tshirt","buttonshirt_S","buttonshirt_L","parka","sweater","Tshirt_LS"]
    down = ["slacks","short","half","jeans","chinos","sweat"]
    outer1 = ["coat","jacket"]
    outer2 = ["coat","jacket","buttonshirt_L"]

    c_flag = 0

    # 乱数で服画像を選定
    b = down[random.randint(0,(len(down)-1))]
    if b == "half" or b == "short":
        up = ["poloshirt","Tshirt","buttonshirt_S"]
        outer1 = ["buttonshirt_S"]
        outer2 = ["buttonshirt_S"]
    else:
        up = ["poloshirt","Tshirt","buttonshirt_S","buttonshirt_L","parka","sweater","Tshirt_LS"]
        outer1 = ["coat","jacket"]
        outer2 = ["coat","jacket","buttonshirt_L"]

    a = up[random.randint(0,(len(up)-1))]

    # 上着を着せるかは1/2
    c_flag = random.randint(0,1)

    if c_flag == 1:
        if a == "buttonshirt_L":
            c = outer1[random.randint(0,(len(outer1)-1))]
        else:
            c = outer2[random.randint(0,(len(outer2)-1))]
        c = os.path.join(DIR,c)
    else:
        c = 0

    a = os.path.join(DIR,a)
    b = os.path.join(DIR,b)

    # ランダムで1枚ずつ抽出
    num1 = os.listdir(a)
    a = os.path.join(a,num1[random.randint(0,len(num1)-1)])

    num2 = os.listdir(b)
    b = os.path.join(b,num2[random.randint(0,len(num2)-1)])

    if c != 0:
        num3 = os.listdir(c)
        c = os.path.join(c,num3[random.randint(0,len(num3)-1)])

    # パスを返す
    return a,b,c