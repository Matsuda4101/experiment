# -*- coding: utf-8 -*-
from pygame import mixer
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import cv2

DIR = "photo_storage"
LABELS1 = os.listdir(DIR)

class Save(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=150, height=500) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        # サブウィンドウの表示位置
        # 画面の真ん中に表示？
        window_width = 150
        window_height = 500
        a= int(int(root2.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root2.winfo_screenheight()/2) -int(window_height/2))
        root2.geometry(f"{window_width}x{window_height}+{a}+{b}")
        # サブウィンドウを最前面に表示
        #root2.attributes("-topmost", True)

        #ウィンドウの設定
        self.master.title("保存先選択")

        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"正しい分類先を\n指定してください",font=("MSゴシック", "12", "bold"),bg="blue",foreground='#ffffff')
        self.label1.pack(fill=tk.X)

        btn1 = tk.Button(self, text='OK', command=lambda:self.save_image(path), font=("Times", "15", "bold"), width=9, height=2)
        btn1.place(anchor=tk.CENTER,x=75,y=470,height=30)

        self.frame1()

    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)

    # 分類画像の保存
    def save_image(self,path):
        self.path = path
        self.num = rdo_sel.get()

        img = cv2.imread(self.path)

        s = os.path.join("photo_storage",LABELS1[self.num])
        #print(s)
        cv2.imwrite("photo_storage/" + LABELS1[self.num]  + "/1 (" + str(len(os.listdir(s))+1) + ").png", img)
        tk.messagebox.showinfo('保存完了', 'システム内に保存しました', parent=root2)

        root2.destroy()

    def frame1(self):
        # ラジオボタンの状態
        global rdo_sel
        rdo_sel = tk.IntVar()
        rdo_txt = ["長袖ボタンシャツ","半袖ボタンシャツ","チノパン","コート","ハーフパンツ","ジャケット","ジーパン","パーカー","ポロシャツ","ショートパンツ","スラックス","スウェット","セーター","半袖Tシャツ","長袖Tシャツ"]

        # フレームの設定
        frame1 = ttk.Frame(root2, width=120, height=380,relief=tk.RIDGE)
        frame1.place(anchor=tk.CENTER,x=75,y=250)

        # ラジオボタンを作成
        for i in range(len(rdo_txt)):
            rdo = tk.Radiobutton(frame1, value=i, variable=rdo_sel, text=rdo_txt[i], command=self.playSE_1) 
            rdo.place(x=5, y=10 + (i * 24))


def select(img_path):
    global root2
    global path
    path = img_path

    root2 = tk.Toplevel()              # root2インスタンスを生成
    # 閉じるボタンの無効化
    root2.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root2.resizable(0, 0)
    f1 = Save(master=root2)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し

if __name__ == "__main__":
    global root2
    root2 = tk.Tk()              # root2インスタンスを生成
    # 閉じるボタンの無効化
    #root2.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root2.resizable(0, 0)
    f1 = Save(master=root2)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し