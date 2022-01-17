# 冬の服画像取得
# -*- coding: utf-8 -*-
import color
import random
import os

import temp_hot
import temp_normal
import temp_cold

DIR = "photo_storage"
list1 = ["jacket","coat","buttonshirt_S","buttonshirt_L"]
list2 = ["Tshirt","Tshirt_LS","buttonshirt_S","buttonshirt_L","sweater","parka","poloshirt"]
list3 = ["jeans","chinos","slacks","sweat","half","short"]

def select(plan,cl,temp,sl):

    c_num = []
    color_cloth = []

    up = []
    down = []
    outer = []
    
    a1 = []
    b1 = []
    c1 = []
    c = 0

    num = "plan"

    # 予定を取得
    with open('UserData/plan.txt',encoding="utf-8") as f:
        plan_list = f.readlines()
        for i in range(len(plan_list)):
            plan_list[i] = plan_list[i].strip()
            if plan == plan_list[i]:
                #print("予定：" + plan)
                num = num + str(i+1)
                break
    
    # 入力された予定で使用する服の取得
    with open("UserData/cloth/" + num + ".txt",encoding="utf-8") as f:
        cloth = f.readlines()
        for i in range(len(cloth)):
            cloth[i] = cloth[i].strip()

    # 取得した服の情報をリストに追加
    j = 0
    for i in range(0,4):
        if cloth[i] == '1':
            outer.append(list1[j])
        j = j + 1
    
    j = 0
    for i in range(4,11):
        if cloth[i] == '1':
            up.append(list2[j])
        j = j + 1

    j = 0
    for i in range(11,17):
        if cloth[i] == '1':
            down.append(list3[j])
        j = j + 1
    
    # 利用者の体感気温情報を取得
    with open('UserData/temp.txt',encoding="utf-8") as f:
        UserTemp = f.readlines()
        for i in range(len(UserTemp)):
            UserTemp[i] = UserTemp[i].strip()
    
    # 暑かった場合
    if temp >= int(UserTemp[0]):
        temp_flag = 1
        # リストから不適切なシャツ類を削除
        i = 0
        while(i < len(up)):
            if up[i] == 'Tshirt_LS':
                i = 0
                up.remove('Tshirt_LS')
                continue
            elif up[i] == 'parka':
                i = 0
                up.remove('parka')
                continue
            elif up[i] == 'sweater':
                i = 0
                up.remove('sweater')
                continue
            elif up[i] == 'buttonshirt_L':
                i = 0
                up.remove('buttonshirt_L')
                continue
            i = i + 1

        # 上着リストから不適切な要素を削除
        i = 0
        while(i < len(outer)):
            if outer[i] == 'coat':
                i = 0
                outer.remove('coat')
                continue
            elif outer[i] == 'jacket':
                i = 0
                outer.remove('jacket')
                continue
            elif outer[i] == 'buttonshirt_L':
                i = 0
                outer.remove('buttonshirt_L')
                continue
            i = i + 1

    # 適温だった場合
    elif int(UserTemp[0]) > temp and temp > int(UserTemp[1]):
        temp_flag = 2
        # リストから不適切なシャツ類を削除
        i = 0
        while(i < len(up)):
            if up[i] == 'poloshirt':
                i = 0
                up.remove('poloshirt')
                continue
            elif up[i] == 'buttonshirt_S':
                i = 0
                up.remove('buttonshirt_S')
                continue
            elif up[i] == 'Tshirt':
                i = 0
                up.remove('Tshirt')
                continue
            i = i + 1

        # リストから不適切なズボン類を削除
        i = 0
        while(i < len(down)):
            if down[i] == 'short':
                i = 0
                down.remove('short')
                continue
            elif down[i] == 'half':
                i = 0
                down.remove('half')
                continue
            i = i + 1
        
        # 上着リストから不適切な要素を削除
        i = 0
        while(i < len(outer)):
            if outer[i] == 'coat':
                i = 0
                outer.remove('coat')
                continue
            elif outer[i] == 'jacket':
                i = 0
                outer.remove('jacket')
                continue
            elif outer[i] == 'buttonshirt_S':
                i = 0
                outer.remove('buttonshirt_S')
                continue
            i = i + 1
        
    # 寒かった場合
    else:
        temp_flag = 3
        # リストから不適切なシャツ類を削除
        i = 0
        while(i < len(up)):
            if up[i] == 'Tshirt':
                i = 0
                up.remove('Tshirt')
                continue
            elif up[i] == 'poloshirt':
                i = 0
                up.remove('poloshirt')
                continue
            elif up[i] == 'buttonshirt_S':
                i = 0
                up.remove('buttonshirt_S')
                continue
            i = i + 1

        # リストから不適切なズボン類を削除
        i = 0
        while(i < len(down)):
            if down[i] == 'short':
                i = 0
                down.remove('short')
                continue
            elif down[i] == 'half':
                i = 0
                down.remove('half')
                continue
            i = i + 1

        # 上着リストから不適切な上着類を削除
        i = 0
        while(i < len(outer)):
            if outer[i] == 'buttonshirt_S':
                i = 0
                outer.remove('buttonshirt_S')
                continue
            elif outer[i] == 'buttonshirt_L':
                i = 0
                outer.remove('buttonshirt_L')
                continue
            i = i + 1

    #print(outer)
    #print(up)
    #print(down)

    # 乱数で服画像を選定
    if temp_flag == 1:
        c_num, a, b, c = temp_hot.hot_choice(up,down,outer,sl)
    elif temp_flag == 2:
        c_num, a, b, c = temp_normal.normal_choice(up,down,outer,sl)
    elif temp_flag == 3:
        c_num, a, b, c = temp_cold.cold_choice(up,down,outer,sl)
    
    print(c_num)

    # 好みの色をランダムで選定した服画像から取得
    random.shuffle(c_num)
    if cl != "no":
        for i in c_num:
            print(i)
            color_cloth = color.color_get(i,cl)
            if len(color_cloth) != 0:
                break
    else:
        i = "0"
    print("リストの中身：",color_cloth)
    

    # 各リストを返す
    if i == a and len(color_cloth) != 0:
        print(1)
        a1 = color_cloth

        for i in os.listdir(b):
            num = os.path.join(b,i)
            b1.append(num)

        if c != 0:
            for i in os.listdir(c):
                num = os.path.join(c,i)
                c1.append(num)

    elif i == b and len(color_cloth) != 0:
        print(2)
        for i in os.listdir(a):
            num = os.path.join(a,i)
            a1.append(num)

        b1 = color_cloth

        if c != 0:
            for i in os.listdir(c):
                num = os.path.join(c,i)
                c1.append(num)
        
    elif i == c and len(color_cloth) != 0:
        print(3)
        for i in os.listdir(a):
            num = os.path.join(a,i)
            a1.append(num)

        for i in os.listdir(b):
            num = os.path.join(b,i)
            b1.append(num)

        c1 = color_cloth
        
    else:
        print("入力した色の服画像がないためランダムで生成します")
        for i in os.listdir(a):
            num = os.path.join(a,i)
            a1.append(num)

        for i in os.listdir(b):
            num = os.path.join(b,i)
            b1.append(num)
        
        if c != 0:
            for i in os.listdir(c):
                num = os.path.join(c,i)
                c1.append(num)

    # print("パス\n",a1,b1,c1)
    # パスを返す
    return a1,b1,c1