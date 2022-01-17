# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
from pygame import mixer
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import cv2
import os

import UI_B
import yomikomi
import sense
import setup_win

class Frame1(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=600, height=400) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        # 画面の真ん中に表示？
        window_width= 600
        window_height= 400
        a= int(int(root.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root.winfo_screenheight()/2) -int(window_height/2))
        root.geometry(f"{window_width}x{window_height}+{a}+{b}")

        #ウィンドウの設定
        self.master.title("自称オートコーディネートシステム")

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"卒研オートコーディネートシステム",font=("MSゴシック", "27", "bold"), foreground="#ffffff",bg="blue")
        self.label1.pack(anchor=tk.CENTER,fill=tk.X,ipady=15)

        # ラベルを作成
        self.label2 = tk.Label(self, text=u"東海大学 情報通信学部 組込みソフトウェア工学科\n撫中研究室 Bチーム",font=("MSゴシック", "15"), foreground="#ffffff",bg="blue")
        self.label2.pack(anchor=tk.CENTER,fill=tk.X,ipady=10)

         # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

         # 実行内容
        self.pack()             # フレームを配置

        #btn = tk.Button(self, text='初期設定', command=self.setup, font=("Times", "10", "bold"), width=10, height=1)
        #btn.place(anchor=tk.CENTER,x=70,y=350,height=50)

        # 各種フレーム・ボタン等を配置
        self.set_frame1()
    
    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)
    
    def change(self):
        self.playSE_1()
        root.destroy()
        UI_B.corde()

    def bunnrui(self):
        self.playSE_1()
        root.destroy()
        yomikomi.nyuuryoku()
    
    def learn(self):
        self.playSE_1()
        root.destroy()
        sense.prefer()

    def setup(self):
        self.playSE_1()
        root.destroy()
        setup_win.setup()

    def set_frame1(self):

        frame1 = ttk.Frame(self, width=300, height=200,relief=tk.RIDGE)
        frame1.place(anchor=tk.CENTER,x=300,y=280)

        btn1 = tk.Button(frame1, text='服画像入力', command=self.bunnrui, font=("Times", "15", "bold"), width=22, height=2)
        btn1.place(anchor=tk.CENTER,x=150,y=40,height=50)

        btn2 = tk.Button(frame1, text='コーデ出力', command=self.change, font=("Times", "15", "bold"), width=22, height=2)
        btn2.place(anchor=tk.CENTER,x=150,y=100,height=50)

        btn3 = tk.Button(frame1, text='好み学習', command=self.learn, font=("Times", "15", "bold"), width=22, height=2)
        btn3.place(anchor=tk.CENTER,x=150,y=160,height=50)

def modoru():      # このファイルが実行されている場合の処理
    global root
    root = tk.Tk()              # rootインスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1 = Frame1(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop() 

if __name__ == "__main__":      # このファイルが実行されている場合の処理
    root = tk.Tk()              # rootインスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1 = Frame1(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタ