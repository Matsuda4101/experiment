# -*- coding: utf-8 -*-
from pygame import mixer
from tkinter import filedialog
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import cv2

DIR = "photo_storage"
LABELS1 = os.listdir(DIR)

flag = 0
file_path =""

class Favorite(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=300, height=100) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        # サブウィンドウの表示位置
        # 画面の真ん中に表示？
        window_width = 300
        window_height = 100
        a= int(int(root3.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root3.winfo_screenheight()/2) -int(window_height/2))
        root3.geometry(f"{window_width}x{window_height}+{a}+{b}")
        # サブウィンドウを最前面に表示
        #root3.attributes("-topmost", True)

        #ウィンドウの設定
        self.master.title("服選択")

        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"服の種類を選択してください",font=("MSゴシック", "12", "bold"),bg="blue",foreground='#ffffff')
        self.label1.pack(fill=tk.X)

        self.frame1()

    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)

    def up(self):
        global flag
        global file_path
        self.playSE_1()
        flag = 1
        idir ='photo_storage' #初期フォルダ
        filetype = [("テキスト","*.png")]
        file_path = tk.filedialog.askopenfilename(filetypes = filetype, initialdir = idir, parent=root3)
        root3.destroy()
        root3.quit()
        return flag, file_path
    
    def down(self):
        global flag
        global file_path
        self.playSE_1()
        flag = 2
        idir ='photo_storage' #初期フォルダ
        filetype = [("テキスト","*.png")]
        file_path = tk.filedialog.askopenfilename(filetypes = filetype, initialdir = idir, parent=root3)
        root3.destroy()
        root3.quit()
        return flag, file_path
    
    def outer(self):
        global flag
        global file_path
        self.playSE_1()
        flag = 3
        idir ='photo_storage' #初期フォルダ
        filetype = [("テキスト","*.png")]
        file_path = tk.filedialog.askopenfilename(filetypes = filetype, initialdir = idir, parent=root3)
        root3.destroy()
        root3.quit()
        return flag, file_path

    def frame1(self):
        # ボタン作成 
        btn1 = tk.Button(root3, text='シャツ類', command=self.up, width=6, height=1, font=("MSゴシック", "15","bold"))
        btn1.place(anchor=tk.CENTER,x=50,y=60,width=90,height=50)

        btn1 = tk.Button(root3, text='ズボン類', command=self.down, width=6, height=1, font=("MSゴシック", "15","bold"))
        btn1.place(anchor=tk.CENTER,x=150,y=60,width=90,height=50)

        btn1 = tk.Button(root3, text='上着類', command=self.outer, width=6, height=1, font=("MSゴシック", "15","bold"))
        btn1.place(anchor=tk.CENTER,x=250,y=60,width=90,height=50)


def select():
    global root3
    global path
    global flag
    global file_path

    root3 = tk.Toplevel()              # root3インスタンスを生成
    # 閉じるボタンの無効化
    root3.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root3.resizable(0, 0)
    f1 = Favorite(master=root3)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し
    
    return flag, file_path

if __name__ == "__main__":
    global root3
    root3 = tk.Tk()              # root2インスタンスを生成
    # 閉じるボタンの無効化
    #root2.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root3.resizable(0, 0)
    f1 = Favorite(master=root3)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し