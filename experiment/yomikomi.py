# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
from pygame import mixer
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import cv2
import os
from tkinter import filedialog
import subprocess

import maingamen
import image_answer
import save_select
import AgeGender

DIR = "photo_storage"
LABELS1 = os.listdir(DIR)
LABELS2 = ["長袖ボタンシャツ","半袖ボタンシャツ","チノパン","コート","ハーフパンツ","ジャケット","ジーパン","パーカー","ポロシャツ","ショートパンツ","スラックス","スウェット","セーター","半袖Tシャツ","長袖Tシャツ"]

#ボタンがクリックされたら実行
class yomikomi(tk.Frame):
    
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=600, height=400) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定
 
        # 画面の真ん中に表示？
        window_width= 600
        window_height= 400
        a= int(int(root.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root.winfo_screenheight()/2) -int(window_height/2))
        root.geometry(f"{window_width}x{window_height}+{a}+{b}")

        #ウィンドウの設定
        self.master.title("服画像入力モード")

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"あなたの服を分類＆保存します！",font=("MSゴシック", "20", "bold"),bg="blue",foreground='#ffffff')
        self.label1.pack(fill=tk.X)
 
        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # 各種フレーム・ボタン等を配置
        self.set_frame1()

    # 効果音
    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)
    
    # 入力方法の選択
    def choice(self):
        self.playSE_1()
        ret = tk.messagebox.askyesno('確認', "カメラから直接入力しますか？")
        if ret == True:
            self.frame = AgeGender.face_age()
            cv2.imwrite("camera_entry_cloth/enter.png",self.frame)
            self.classification("camera_entry_cloth/enter.png")
        elif ret == False:
            self.file_select()

    # 入力画像を検索
    def file_select(self):
        idir ='fashion_photo' #初期フォルダ
        filetype = [("テキスト","*.png")]
        file_path = tk.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
        #input_box.insert(tk.END, file_path) #結果を表示
        self.classification(file_path)

    # 入力画像を分類
    def classification(self,path):
        self.path = path
        ans = image_answer.answer(self.path)
        sen = "これは" + ans + "で合っていますか？"
        ret = tk.messagebox.askyesno('判定結果', sen)
        if ret == True:
            self.save_image(ans,self.path)
        elif ret == False:
            save_select.select(self.path)
    
    # 分類画像の保存
    def save_image(self,ans,path):
        self.ans = ans
        self.path = path

        for i in range(len(LABELS1)):
            if LABELS2[i] == self.ans:
                img = cv2.imread(self.path)

                s = os.path.join("photo_storage",LABELS1[i])
                #print(s)
                cv2.imwrite("photo_storage/" + LABELS1[i]  + "/1 (" + str(len(os.listdir(s))+1) + ").png", img)
                tk.messagebox.showinfo('保存完了', 'システム内に保存しました', parent=root)
                break

    def image_edit(self):
        self.playSE_1()
        #テスト画像ファイルの表示
        subprocess.run('explorer {}'.format("photo_storage"))

    # 戻るボタン
    def back(self):
        self.playSE_1()
        root.destroy()
        maingamen.modoru()
        

    def set_frame1(self):
        frame1 = ttk.Frame(root, width=300, height=200,relief=tk.RIDGE)
        frame1.place(anchor=tk.CENTER,x=300,y=220)
        global input_box
        #入力欄の作成
        #input_box = tk.Entry(width=60)
        #input_box.place(x=750, y=180)

        #ラベルの作成
        #input_label = tk.Label(text="結果")
        #input_label.place(anchor=tk.CENTER,x=750, y=150)

        btn1 = tk.Button(frame1, text='入力する服画像の選択', command=self.choice, font=("Times", "15", "bold"), width=22, height=1)
        btn1.place(anchor=tk.CENTER,x=150,y=40,height=50)

        btn2 = tk.Button(frame1, text='保存画像の閲覧・編集', command=self.image_edit, font=("Times", "15", "bold"), width=22, height=1)
        btn2.place(anchor=tk.CENTER,x=150,y=100,height=50)

        btn3 = tk.Button(frame1, text='戻る', command=self.back, font=("Times", "15", "bold"), width=22, height=1)
        btn3.place(anchor=tk.CENTER,x=150,y=160,height=50)


#if __name__ == "__main__":
def nyuuryoku():
    global root    
    root = tk.Tk()              # rootインスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1 = yomikomi(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop() 

if __name__ == "__main__":
    global root    
    root = tk.Tk()              # rootインスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1 = yomikomi(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop() 