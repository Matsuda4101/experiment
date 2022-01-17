# メイン画面で「B」を入力された場合の処理
# -*- coding: utf-8 -*-
import AgeGender
import os
import random
import cv2
import matplotlib.pyplot as plt 
import tkinter as tk
import tkinter.messagebox

import image_connect
import temp_select
import fashion_select
import sense_select
import favorite_cloth

fc = ["派手","シンプル","暗め"]
se = ["好みに合わない","好みに合う"]

def nice_fashion(plan,color,fashion,place):

    global img
    global img1
    global img2
    global img3
    global dst

    up = []
    down = []
    outer =[]

    flag1 = 0
    flag2 = 0

    max_per = 0
    max_img = 0
    max_img1 = 0
    max_img2 = 0
    max_img3 = 0
    max_dst = 0

    num = 0

    # モデルの存在確認
    ex = os.path.isfile("2.hdf5")
    print(ex)

    # 着たい服があれば入力できる
    ret = tk.messagebox.askyesno('確認', "服を1着のみ指定できます\n選択しますか？")
    if ret == True:
        sl, favorite_path = favorite_cloth.select()
    else:
        sl = 0
        favorite_path = 0

    while True:

        # 好みの季節と色の服画像を取得
        up,down,outer = temp_select.cloth_choice(plan,place,color,sl)

        for i in range(10):
            # 一定回数探しても見つからない場合は、そこまでの最大値を返す
            if num >= 20:
                print("指定階数を超えたため最大値を返します：max_per=" + str(max_per))
                return max_img, max_img1, max_img2, max_img3, max_dst

            # シャツ類のパスを取得
            if sl == 1:
                a = favorite_path
            else:
                num1 = random.randint(0,len(up)-1)   # 上
                a = up[num1]
                
    
            # ズボン類のパスを取得
            if sl == 2:
                b = favorite_path
            else:
                num1 = random.randint(0,len(down)-1)   # 下
                b = down[num1]

            # 上着類のパスを取得
            if sl == 3:
                c = favorite_path
            else:
                if not outer:
                    c = 0
                else:
                    num1 = random.randint(0,len(outer)-1)   # 上着
                    c = outer[num1]

            print(a)
            print(b)
            print(c)

            # 服画像を結合させる
            img, img1, img2, img3, dst = image_connect.get_concat_v(a,b,c)

            # 結合した画像の分類
            category, per = fashion_select.answer(fashion,img)

            # 好みに合っているのかチェック
            if str(ex) == "True":
                flag2 = 1
                sense = sense_select.answer(img)

            # 入力と一致したらループを抜ける
            print("入力されたファッション：" + fc[int(fashion)])

            if flag2 == 0:
                print("分類結果：" + fc[int(category)] + "\n")
                if int(category) == int(fashion):
                    flag1 = 1
                    break

            elif flag2 == 1:
                print("分類結果：" + fc[int(category)] + " ＆ " + se[sense] + "\n")
                if int(category) == int(fashion) and sense == 1 :
                    flag1 = 1
                    break

            if max_per < per:
                max_per = per
                max_img = img
                max_img1 = img1
                max_img2 = img2
                max_img3 = img3
                max_dst = dst

            num = num + 1

        if flag1 == 1:
            break
    
    return img, img1, img2, img3, dst