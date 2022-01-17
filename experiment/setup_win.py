# -*- coding: utf-8 -*-
from pygame import mixer
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

import maingamen

class Set(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=250, height=200) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        # サブウィンドウの表示位置
        # 画面の真ん中に表示？
        window_width = 250
        window_height = 200
        a= int(int(root2.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root2.winfo_screenheight()/2) -int(window_height/2))
        root2.geometry(f"{window_width}x{window_height}+{a}+{b}")
        # サブウィンドウを最前面に表示
        #root2.attributes("-topmost", True)

        #ウィンドウの設定
        self.master.title("ユーザーデータ登録")

        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"初期設定を行ってください",font=("MSゴシック", "12", "bold"),bg="blue",foreground='#ffffff')
        self.label1.pack(fill=tk.X)

        btn1 = tk.Button(self, text='OK', command=self.OK, font=("Times", "13", "bold"), width=8, height=2)
        btn1.place(anchor=tk.CENTER,x=125,y=180,height=25)

        self.frame1()

    def OK(self):
        self.playSE_1()

        num1 = str(combobox1.get()) + "\n"
        num2 = str(combobox2.get())
        plan = [num1,num2]
        # 「予定」の保存
        with open('UserData/user_data.txt',encoding="utf-8", mode='w') as f:
            f.writelines(plan)

        tk.messagebox.showinfo('保存完了', 'データを保存しました')
        root2.destroy()
        maingamen.modoru()

    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)
    
    def playSE_2(self,event):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)

    def frame1(self):

        global c_text1
        global c_text2

        global combobox1
        global combobox2

        c_text1 = ["～10歳","～20歳","～30歳","～40歳","～50歳","～60歳","～70歳","～80歳","～90歳","～100歳","101歳～"]
        c_text2 = ["男","女","その他"]

        # フレームの設定
        frame1 = ttk.Frame(root2, width=200, height=130,relief=tk.RIDGE)
        frame1.place(anchor=tk.CENTER,x=125,y=95)

        self.label2 = tk.Label(frame1, text=u"年齢",font=("MSゴシック", "15"),bg="whitesmoke")
        self.label2.place(anchor=tk.CENTER,x=50,y=40)

        # コンボボックスを作成
        combobox1 = ttk.Combobox(frame1,height=11,values=c_text1, justify="center", state="readonly", font=("MSゴシック", "12", "bold"))
        combobox1.bind("<<ComboboxSelected>>",self.playSE_2)
        combobox1.place(anchor=tk.CENTER,x=120,y=40,width=80,height=25)

        self.label3 = tk.Label(frame1, text=u"性別",font=("MSゴシック", "15"),bg="whitesmoke")
        self.label3.place(anchor=tk.CENTER,x=50,y=90)

        # コンボボックスを作成
        combobox2 = ttk.Combobox(frame1,height=3,values=c_text2, justify="center", state="readonly", font=("MSゴシック", "12", "bold"))
        combobox2.bind("<<ComboboxSelected>>",self.playSE_2)
        combobox2.place(anchor=tk.CENTER,x=120,y=90,width=80,height=25)


def setup():
    global root2

    root2 = tk.Tk()              # root2インスタンスを生成
    # 閉じるボタンの無効化
    root2.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root2.resizable(0, 0)
    f1 = Set(master=root2)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し

if __name__ == "__main__":
    global root2
    root2 = tk.Tk()              # root2インスタンスを生成
    # 閉じるボタンの無効化
    #root2.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root2.resizable(0, 0)
    f1 = Set(master=root2)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し