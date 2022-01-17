# -*- coding: utf-8 -*-
from pygame import mixer
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

import UI_B

class SubWindow(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=1000, height=700) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        # サブウィンドウの表示位置
        # 画面の真ん中に表示？
        window_width= 1000
        window_height= 700
        a= int(int(root.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root.winfo_screenheight()/2) -int(window_height/2))
        root.geometry(f"{window_width}x{window_height}+{a}+{b}")
        # サブウィンドウを最前面に表示
        #root.attributes("-topmost", True)

        #ウィンドウの設定
        self.master.title("設定")

        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # ラベルを作成
        self.label1 = tk.Label(root, text=u"予定・出力服の設定",font=("MSゴシック", "15", "bold"))
        self.label1.place(anchor=tk.CENTER,x=500,y=15)
    
        # キャンセルボタン作成 
        btn1 = tk.Button(root, text='キャンセル', command=self.cansel, width=10, height=1, font=("MSゴシック", "10"))
        btn1.place(anchor=tk.CENTER,x=450,y=680)

        # OKボタン作成 
        btn1 = tk.Button(root, text='OK', command=self.OK, width=10, height=1, font=("MSゴシック", "10"))
        btn1.place(anchor=tk.CENTER,x=550,y=680)

        # 予定データを読み込む
        global plan

        with open('UserData/plan.txt',encoding="utf-8") as f:
            plan = f.readlines()
            for i in range(len(plan)):
                plan[i] = plan[i].strip()
            #print(plan)

        # 各種出力服データを読み込む
        global cloth1
        global cloth2
        global cloth3
        global cloth4

        with open('UserData/cloth/plan1.txt',encoding="utf-8") as f:
            cloth1 = f.readlines()
            for i in range(len(cloth1)):
                cloth1[i] = cloth1[i].strip()
            #print(cloth1)

        with open('UserData/cloth/plan2.txt',encoding="utf-8") as f:
            cloth2 = f.readlines()
            for i in range(len(cloth2)):
                cloth2[i] = cloth2[i].strip()
            #print(cloth2)

        with open('UserData/cloth/plan3.txt',encoding="utf-8") as f:
            cloth3 = f.readlines()
            for i in range(len(cloth3)):
                cloth3[i] = cloth3[i].strip()
            #print(cloth3)

        with open('UserData/cloth/plan4.txt',encoding="utf-8") as f:
            cloth4 = f.readlines()
            for i in range(len(cloth4)):
                cloth4[i] = cloth4[i].strip()
            #print(cloth4)

        # テキストボックスに使用する衣服リスト
        global chk_txt1
        chk_txt1 = ["ジャケット","コート","半袖ボタンシャツ","長袖ボタンシャツ"]
        global chk_txt2
        chk_txt2 = ["半袖Tシャツ","長袖Tシャツ","半袖ボタンシャツ","長袖ボタンシャツ","セーター","パーカー","ポロシャツ"]
        global chk_txt3
        chk_txt3 = ["ジーパン","チノパン","スラックス","スウェット","ハーフパンツ","ショートパンツ"]

        self.frame1()
        self.frame2()
        self.frame3()
        self.frame4()
        self.frame5()
        
    # クリック音
    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)
    
    # 全選択ボタンが押されたとき
    def all1(self,num):
        self.num = num
        self.playSE_1()
        for i in range(0,4):
            if self.num == 1:
                chk_bln1[i].set(True)
            elif self.num == 2:
                chk_bln2[i].set(True)
            elif self.num == 3:
                chk_bln3[i].set(True)
            else:
                chk_bln4[i].set(True)
    
    def all2(self,num):
        self.num = num
        self.playSE_1()
        for i in range(4,11):
            if self.num == 1:
                chk_bln1[i].set(True)
            elif self.num == 2:
                chk_bln2[i].set(True)
            elif self.num == 3:
                chk_bln3[i].set(True)
            else:
                chk_bln4[i].set(True)
    
    def all3(self,num):
        self.num = num
        self.playSE_1()
        for i in range(11,17):
            if self.num == 1:
                chk_bln1[i].set(True)
            elif self.num == 2:
                chk_bln2[i].set(True)
            elif self.num == 3:
                chk_bln3[i].set(True)
            else:
                chk_bln4[i].set(True)


    # サブウィンドウを閉じる
    def cansel(self):
        self.playSE_1()
        global sub_flag
        sub_flag = 0
        ret = tk.messagebox.askyesno('確認', '保存せず終了しますか？')
        if ret == True:
            root.destroy()
            UI_B.corde()
    
    # 変更内容を保存して戻る
    def OK(self):
        self.playSE_1()
        global sub_flag
        sub_flag = 0

        # シャツ類ズボン類のチェック
        # チェックが0個ならreturn
        check_num = 0
        # chk_bln1
        for j in range(4,11):
            #print(chk_bln1[j].get())
            if str(chk_bln1[j].get()) == "False":
                check_num = check_num + 1
        #print(str(check_num))
        if check_num == 7:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0

        for j in range(11,17):
            #print(chk_bln1[j].get())
            if str(chk_bln1[j].get()) == "False":
                check_num = check_num + 1
        #print(str(check_num)+"\n")
        if check_num == 6:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0
        
        # chk_bln2
        for j in range(4,11):
            if str(chk_bln2[j].get()) == "False":
                check_num = check_num + 1
        if check_num == 7:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0

        for j in range(11,17):
            if str(chk_bln2[j].get()) == "False":
                check_num = check_num + 1
        if check_num == 6:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0
        
        # chk_bln3
        for j in range(4,11):
            if str(chk_bln3[j].get()) == "False":
                check_num = check_num + 1
        if check_num == 7:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0

        for j in range(11,17):
            if str(chk_bln3[j].get()) == "False":
                check_num = check_num + 1
        if check_num == 6:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0
        
        # chk_bln4
        for j in range(4,11):
            if str(chk_bln4[j].get()) == "False":
                check_num = check_num + 1
        if check_num == 7:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0

        for j in range(11,17):
            if str(chk_bln4[j].get()) == "False":
                check_num = check_num + 1
        if check_num == 6:
            tk.messagebox.showerror('エラー', 'シャツ＆ズボン類は\n最低1種類以上選択してください')
            return
        else:
            check_num = 0


        # 「予定」の保存
        with open('UserData/plan.txt',encoding="utf-8", mode='w') as f:
            for i in range(4):
                plan[i] = txt_box[i].get() + "\n"
            f.writelines(plan)

        # 予定別各出力服の変更
        with open('UserData/cloth/plan1.txt',encoding="utf-8", mode='w') as f:
            for i in range(len(chk_bln1)):
                if str(chk_bln1[i].get()) == "True":
                    cloth1[i] = "1\n"
                else:
                    cloth1[i] = "0\n"
            f.writelines(cloth1)

        with open('UserData/cloth/plan2.txt',encoding="utf-8", mode='w') as f:
            for i in range(len(chk_bln2)):
                if str(chk_bln2[i].get()) == "True":
                    cloth2[i] = "1\n"
                else:
                    cloth2[i] = "0\n"
            f.writelines(cloth2)
        
        with open('UserData/cloth/plan3.txt',encoding="utf-8", mode='w') as f:
            for i in range(len(chk_bln3)):
                if str(chk_bln3[i].get()) == "True":
                    cloth3[i] = "1\n"
                else:
                    cloth3[i] = "0\n"
            f.writelines(cloth3)
        
        with open('UserData/cloth/plan4.txt',encoding="utf-8", mode='w') as f:
            for i in range(len(chk_bln4)):
                if str(chk_bln4[i].get()) == "True":
                    cloth4[i] = "1\n"
                else:
                    cloth4[i] = "0\n"
            f.writelines(cloth4)

        # 体感気温の保存
        with open('UserData/temp.txt',encoding="utf-8", mode='w') as f:
            for i in range(len(txt_box5)):
                self.UserTemp[i] = txt_box5[i].get() + "\n"

            if int(self.UserTemp[0]) <= int(self.UserTemp[1]):
                tk.messagebox.showerror('エラー', '気温は正しく入力してください')
                return
            f.writelines(self.UserTemp)

        tk.messagebox.showinfo('保存完了', '変更内容を保存しました')
        
        # 再読み込み
        root.destroy()
        UI_B.corde()

    # 予定1フレーム
    def frame1(self):

        # チェックボックスのグローバル変数化
        global chk_bln1
        global chk_1
        # チェックボックスON/OFFの状態
        chk_bln1 = {}
        chk_1 = {}

        # フレームの設定
        frame1 = ttk.Frame(root, width=230, height=400,relief=tk.RIDGE)
        frame1.place(anchor=tk.CENTER,x=140,y=230)

        # テキストボックスを作成
        global txt_box
        txt_box = {}
        txt_box[0] = tk.Entry(frame1, font=("MSゴシック", "13", "bold"),justify="center",bg="blue",foreground="#ffffff")
        txt_box[0].place(anchor=tk.CENTER,x=115,y=12,width=230,height=20)
        txt_box[0].insert(0, plan[0])

        # ラベルを作成
        self.label1_1 = tk.Label(frame1, text=u"上着",font=("MSゴシック", "12", "bold"))
        self.label1_1.place(x=5,y=22)

        # 全選択ボタン
        all_select_1_1 = tk.Button(frame1, text='全選択', command=lambda:self.all1(1), width=6, height=1, font=("MSゴシック", "10"))
        all_select_1_1.place(x=50,y=22)

        # チェックボタンを配置
        chk_bln1[0] = tk.BooleanVar()
        chk_1[0] = tk.Checkbutton(frame1, variable=chk_bln1[0], text=chk_txt1[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[0].place(x=10, y=45 + (0 * 20))

        chk_bln1[1] = tk.BooleanVar()
        chk_1[1] = tk.Checkbutton(frame1, variable=chk_bln1[1], text=chk_txt1[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[1].place(x=120, y=45 + (0 * 20))

        chk_bln1[2] = tk.BooleanVar()
        chk_1[2] = tk.Checkbutton(frame1, variable=chk_bln1[2], text=chk_txt1[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[2].place(x=10, y=45 + (1 * 20))

        chk_bln1[3] = tk.BooleanVar()
        chk_1[3] = tk.Checkbutton(frame1, variable=chk_bln1[3], text=chk_txt1[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[3].place(x=10, y=45 + (2 * 20))

        # ラベルを作成
        self.label1_2 = tk.Label(frame1, text=u"シャツ類",font=("MSゴシック", "12", "bold"))
        self.label1_2.place(x=5,y=117)

        # 全選択ボタン
        all_select_1_2 = tk.Button(frame1, text='全選択', command=lambda:self.all2(1), width=6, height=1, font=("MSゴシック", "10"))
        all_select_1_2.place(x=85,y=117)

        # チェックボタンを配置
        chk_bln1[4] = tk.BooleanVar()
        chk_1[4] = tk.Checkbutton(frame1, variable=chk_bln1[4], text=chk_txt2[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[4].place(x=10, y=140 + (0 * 20))

        chk_bln1[5] = tk.BooleanVar()
        chk_1[5] = tk.Checkbutton(frame1, variable=chk_bln1[5], text=chk_txt2[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[5].place(x=10, y=140 + (1 * 20))

        chk_bln1[6] = tk.BooleanVar()
        chk_1[6] = tk.Checkbutton(frame1, variable=chk_bln1[6], text=chk_txt2[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[6].place(x=10, y=140 + (2 * 20))

        chk_bln1[7] = tk.BooleanVar()
        chk_1[7] = tk.Checkbutton(frame1, variable=chk_bln1[7], text=chk_txt2[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[7].place(x=10, y=140 + (3 * 20))

        chk_bln1[8] = tk.BooleanVar()
        chk_1[8] = tk.Checkbutton(frame1, variable=chk_bln1[8], text=chk_txt2[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[8].place(x=10, y=140 + (4 * 20))

        chk_bln1[9] = tk.BooleanVar()
        chk_1[9] = tk.Checkbutton(frame1, variable=chk_bln1[9], text=chk_txt2[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[9].place(x=120, y=140 + (4 * 20))

        chk_bln1[10] = tk.BooleanVar()
        chk_1[10] = tk.Checkbutton(frame1, variable=chk_bln1[10], text=chk_txt2[6], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[10].place(x=10, y=140 + (5 * 20))

        # ラベルを作成
        self.label1_3 = tk.Label(frame1, text=u"ズボン類",font=("MSゴシック", "12", "bold"))
        self.label1_3.place(x=5,y=272)

        # 全選択ボタン
        all_select_1_3 = tk.Button(frame1, text='全選択', command=lambda:self.all3(1), width=6, height=1, font=("MSゴシック", "10"))
        all_select_1_3.place(x=85,y=272)

        # チェックボタンを配置
        chk_bln1[11] = tk.BooleanVar()
        chk_1[11] = tk.Checkbutton(frame1, variable=chk_bln1[11], text=chk_txt3[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[11].place(x=10, y=295 + (0 * 20))

        chk_bln1[12] = tk.BooleanVar()
        chk_1[12] = tk.Checkbutton(frame1, variable=chk_bln1[12], text=chk_txt3[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[12].place(x=120, y=295 + (0 * 20))

        chk_bln1[13] = tk.BooleanVar()
        chk_1[13] = tk.Checkbutton(frame1, variable=chk_bln1[13], text=chk_txt3[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[13].place(x=10, y=295 + (1 * 20))

        chk_bln1[14] = tk.BooleanVar()
        chk_1[14] = tk.Checkbutton(frame1, variable=chk_bln1[14], text=chk_txt3[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[14].place(x=120, y=295 + (1 * 20))

        chk_bln1[15] = tk.BooleanVar()
        chk_1[15] = tk.Checkbutton(frame1, variable=chk_bln1[15], text=chk_txt3[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[15].place(x=10, y=295 + (2 * 20))

        chk_bln1[16] = tk.BooleanVar()
        chk_1[16] = tk.Checkbutton(frame1, variable=chk_bln1[16], text=chk_txt3[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_1[16].place(x=10, y=295 + (3 * 20))

        for i in range(len(cloth1)):
            if cloth1[i] == "1":
                chk_bln1[i].set(True)

    # 予定2フレーム
    def frame2(self):

        # チェックボックスのグローバル変数化
        global chk_bln2
        global chk_2
        chk_2 = {}
        # チェックボックスON/OFFの状態
        chk_bln2 = {}

        # フレームの設定
        frame2 = ttk.Frame(root, width=230, height=400,relief=tk.RIDGE)
        frame2.place(anchor=tk.CENTER,x=380,y=230)

        # テキストボックスを作成
        txt_box[1] = tk.Entry(frame2,font=("MSゴシック", "13", "bold"),justify="center",bg="blue",foreground="#ffffff")
        txt_box[1].place(anchor=tk.CENTER,x=115,y=12,width=230,height=20)
        txt_box[1].insert(0, plan[1])

        # ラベルを作成
        self.label1_1 = tk.Label(frame2, text=u"上着",font=("MSゴシック", "12", "bold"))
        self.label1_1.place(x=5,y=22)

        # 全選択ボタン
        all_select_2_1 = tk.Button(frame2, text='全選択', command=lambda:self.all1(2), width=6, height=1, font=("MSゴシック", "10"))
        all_select_2_1.place(x=50,y=22)

        # チェックボタンを配置
        chk_bln2[0] = tk.BooleanVar()
        chk_2[0] = tk.Checkbutton(frame2, variable=chk_bln2[0], text=chk_txt1[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[0].place(x=10, y=45 + (0 * 20))

        chk_bln2[1] = tk.BooleanVar()
        chk_2[1] = tk.Checkbutton(frame2, variable=chk_bln2[1], text=chk_txt1[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[1].place(x=120, y=45 + (0 * 20))

        chk_bln2[2] = tk.BooleanVar()
        chk_2[2] = tk.Checkbutton(frame2, variable=chk_bln2[2], text=chk_txt1[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[2].place(x=10, y=45 + (1 * 20))

        chk_bln2[3] = tk.BooleanVar()
        chk_2[3] = tk.Checkbutton(frame2, variable=chk_bln2[3], text=chk_txt1[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[3].place(x=10, y=45 + (2 * 20))

        # ラベルを作成
        self.label1_2 = tk.Label(frame2, text=u"シャツ類",font=("MSゴシック", "12", "bold"))
        self.label1_2.place(x=5,y=117)

        # 全選択ボタン
        all_select_2_2 = tk.Button(frame2, text='全選択', command=lambda:self.all2(2), width=6, height=1, font=("MSゴシック", "10"))
        all_select_2_2.place(x=85,y=117)

        # チェックボタンを配置
        chk_bln2[4] = tk.BooleanVar()
        chk_2[4] = tk.Checkbutton(frame2, variable=chk_bln2[4], text=chk_txt2[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[4].place(x=10, y=140 + (0 * 20))

        chk_bln2[5] = tk.BooleanVar()
        chk_2[5] = tk.Checkbutton(frame2, variable=chk_bln2[5], text=chk_txt2[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[5].place(x=10, y=140 + (1 * 20))

        chk_bln2[6] = tk.BooleanVar()
        chk_2[6] = tk.Checkbutton(frame2, variable=chk_bln2[6], text=chk_txt2[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[6].place(x=10, y=140 + (2 * 20))

        chk_bln2[7] = tk.BooleanVar()
        chk_2[7] = tk.Checkbutton(frame2, variable=chk_bln2[7], text=chk_txt2[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[7].place(x=10, y=140 + (3 * 20))

        chk_bln2[8] = tk.BooleanVar()
        chk_2[8] = tk.Checkbutton(frame2, variable=chk_bln2[8], text=chk_txt2[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[8].place(x=10, y=140 + (4 * 20))

        chk_bln2[9] = tk.BooleanVar()
        chk_2[9] = tk.Checkbutton(frame2, variable=chk_bln2[9], text=chk_txt2[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[9].place(x=120, y=140 + (4 * 20))

        chk_bln2[10] = tk.BooleanVar()
        chk_2[10] = tk.Checkbutton(frame2, variable=chk_bln2[10], text=chk_txt2[6], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[10].place(x=10, y=140 + (5 * 20))

        # ラベルを作成
        self.label1_3 = tk.Label(frame2, text=u"ズボン類",font=("MSゴシック", "12", "bold"))
        self.label1_3.place(x=5,y=272)

        # 全選択ボタン
        all_select_2_3 = tk.Button(frame2, text='全選択', command=lambda:self.all3(2), width=6, height=1, font=("MSゴシック", "10"))
        all_select_2_3.place(x=85,y=272)

        # チェックボタンを配置
        chk_bln2[11] = tk.BooleanVar()
        chk_2[11] = tk.Checkbutton(frame2, variable=chk_bln2[11], text=chk_txt3[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[11].place(x=10, y=295 + (0 * 20))

        chk_bln2[12] = tk.BooleanVar()
        chk_2[12] = tk.Checkbutton(frame2, variable=chk_bln2[12], text=chk_txt3[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[12].place(x=120, y=295 + (0 * 20))

        chk_bln2[13] = tk.BooleanVar()
        chk_2[13] = tk.Checkbutton(frame2, variable=chk_bln2[13], text=chk_txt3[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[13].place(x=10, y=295 + (1 * 20))

        chk_bln2[14] = tk.BooleanVar()
        chk_2[14] = tk.Checkbutton(frame2, variable=chk_bln2[14], text=chk_txt3[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[14].place(x=120, y=295 + (1 * 20))

        chk_bln2[15] = tk.BooleanVar()
        chk_2[15] = tk.Checkbutton(frame2, variable=chk_bln2[15], text=chk_txt3[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[15].place(x=10, y=295 + (2 * 20))

        chk_bln2[16] = tk.BooleanVar()
        chk_2[16] = tk.Checkbutton(frame2, variable=chk_bln2[16], text=chk_txt3[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_2[16].place(x=10, y=295 + (3 * 20))

        for i in range(len(cloth2)):
            if cloth2[i] == "1":
                chk_bln2[i].set(True)
    
    # 予定3フレーム
    def frame3(self):

        # チェックボックスのグローバル変数化
        global chk_bln3
        global chk_3
        chk_3 = {}
        # チェックボックスON/OFFの状態
        chk_bln3 = {}

        # フレームの設定
        frame3 = ttk.Frame(root, width=230, height=400,relief=tk.RIDGE)
        frame3.place(anchor=tk.CENTER,x=620,y=230)

        # テキストボックスを作成
        txt_box[2] = tk.Entry(frame3, font=("MSゴシック", "13", "bold"),justify="center",bg="blue",foreground="#ffffff")
        txt_box[2].place(anchor=tk.CENTER,x=115,y=12,width=230,height=20)
        txt_box[2].insert(0, plan[2])

        # ラベルを作成
        self.label1_1 = tk.Label(frame3, text=u"上着",font=("MSゴシック", "12", "bold"))
        self.label1_1.place(x=5,y=22)

        # 全選択ボタン
        all_select_3_1 = tk.Button(frame3, text='全選択', command=lambda:self.all1(3), width=6, height=1, font=("MSゴシック", "10"))
        all_select_3_1.place(x=50,y=22)

        # チェックボタンを配置
        chk_bln3[0] = tk.BooleanVar()
        chk_3[0] = tk.Checkbutton(frame3, variable=chk_bln3[0], text=chk_txt1[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[0].place(x=10, y=45 + (0 * 20))

        chk_bln3[1] = tk.BooleanVar()
        chk_3[1] = tk.Checkbutton(frame3, variable=chk_bln3[1], text=chk_txt1[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[1].place(x=120, y=45 + (0 * 20))

        chk_bln3[2] = tk.BooleanVar()
        chk_3[2] = tk.Checkbutton(frame3, variable=chk_bln3[2], text=chk_txt1[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[2].place(x=10, y=45 + (1 * 20))

        chk_bln3[3] = tk.BooleanVar()
        chk_3[3] = tk.Checkbutton(frame3, variable=chk_bln3[3], text=chk_txt1[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[3].place(x=10, y=45 + (2 * 20))

        # ラベルを作成
        self.label1_2 = tk.Label(frame3, text=u"シャツ類",font=("MSゴシック", "12", "bold"))
        self.label1_2.place(x=5,y=117)

        # 全選択ボタン
        all_select_3_2 = tk.Button(frame3, text='全選択', command=lambda:self.all2(3), width=6, height=1, font=("MSゴシック", "10"))
        all_select_3_2.place(x=85,y=117)

        # チェックボタンを配置
        chk_bln3[4] = tk.BooleanVar()
        chk_3[4] = tk.Checkbutton(frame3, variable=chk_bln3[4], text=chk_txt2[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[4].place(x=10, y=140 + (0 * 20))

        chk_bln3[5] = tk.BooleanVar()
        chk_3[5] = tk.Checkbutton(frame3, variable=chk_bln3[5], text=chk_txt2[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[5].place(x=10, y=140 + (1 * 20))

        chk_bln3[6] = tk.BooleanVar()
        chk_3[6] = tk.Checkbutton(frame3, variable=chk_bln3[6], text=chk_txt2[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[6].place(x=10, y=140 + (2 * 20))

        chk_bln3[7] = tk.BooleanVar()
        chk_3[7] = tk.Checkbutton(frame3, variable=chk_bln3[7], text=chk_txt2[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[7].place(x=10, y=140 + (3 * 20))

        chk_bln3[8] = tk.BooleanVar()
        chk_3[8] = tk.Checkbutton(frame3, variable=chk_bln3[8], text=chk_txt2[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[8].place(x=10, y=140 + (4 * 20))

        chk_bln3[9] = tk.BooleanVar()
        chk_3[9] = tk.Checkbutton(frame3, variable=chk_bln3[9], text=chk_txt2[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[9].place(x=120, y=140 + (4 * 20))

        chk_bln3[10] = tk.BooleanVar()
        chk_3[10] = tk.Checkbutton(frame3, variable=chk_bln3[10], text=chk_txt2[6], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[10].place(x=10, y=140 + (5 * 20))

        # ラベルを作成
        self.label1_3 = tk.Label(frame3, text=u"ズボン類",font=("MSゴシック", "12", "bold"))
        self.label1_3.place(x=5,y=272)

        # 全選択ボタン
        all_select_3_3 = tk.Button(frame3, text='全選択', command=lambda:self.all3(3), width=6, height=1, font=("MSゴシック", "10"))
        all_select_3_3.place(x=85,y=272)

        # チェックボタンを配置
        chk_bln3[11] = tk.BooleanVar()
        chk_3[11] = tk.Checkbutton(frame3, variable=chk_bln3[11], text=chk_txt3[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[11].place(x=10, y=295 + (0 * 20))

        chk_bln3[12] = tk.BooleanVar()
        chk_3[12] = tk.Checkbutton(frame3, variable=chk_bln3[12], text=chk_txt3[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[12].place(x=120, y=295 + (0 * 20))

        chk_bln3[13] = tk.BooleanVar()
        chk_3[13] = tk.Checkbutton(frame3, variable=chk_bln3[13], text=chk_txt3[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[13].place(x=10, y=295 + (1 * 20))

        chk_bln3[14] = tk.BooleanVar()
        chk_3[14] = tk.Checkbutton(frame3, variable=chk_bln3[14], text=chk_txt3[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[14].place(x=120, y=295 + (1 * 20))

        chk_bln3[15] = tk.BooleanVar()
        chk_3[15] = tk.Checkbutton(frame3, variable=chk_bln3[15], text=chk_txt3[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[15].place(x=10, y=295 + (2 * 20))

        chk_bln3[16] = tk.BooleanVar()
        chk_3[16] = tk.Checkbutton(frame3, variable=chk_bln3[16], text=chk_txt3[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_3[16].place(x=10, y=295 + (3 * 20))

        for i in range(len(cloth3)):
            if cloth3[i] == "1":
                chk_bln3[i].set(True)

    # 予定4フレーム
    def frame4(self):

        # チェックボックスのグローバル変数化
        global chk_bln4
        global chk_4
        chk_4 = {}
        # チェックボックスON/OFFの状態
        chk_bln4 = {}

        # フレームの設定
        frame4 = ttk.Frame(root, width=230, height=400,relief=tk.RIDGE)
        frame4.place(anchor=tk.CENTER,x=860,y=230)

        # テキストボックスを作成
        txt_box[3] = tk.Entry(frame4, font=("MSゴシック", "13", "bold"),justify="center",bg="blue",foreground="#ffffff")
        txt_box[3].place(anchor=tk.CENTER,x=115,y=12,width=230,height=20)
        txt_box[3].insert(0, plan[3])

        # ラベルを作成
        self.label1_1 = tk.Label(frame4, text=u"上着",font=("MSゴシック", "12", "bold"))
        self.label1_1.place(x=5,y=22)

        # 全選択ボタン
        all_select_4_1 = tk.Button(frame4, text='全選択', command=lambda:self.all1(4), width=6, height=1, font=("MSゴシック", "10"))
        all_select_4_1.place(x=50,y=22)

        # チェックボタンを配置
        chk_bln4[0] = tk.BooleanVar()
        chk_4[0] = tk.Checkbutton(frame4, variable=chk_bln4[0], text=chk_txt1[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[0].place(x=10, y=45 + (0 * 20))

        chk_bln4[1] = tk.BooleanVar()
        chk_4[1] = tk.Checkbutton(frame4, variable=chk_bln4[1], text=chk_txt1[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[1].place(x=120, y=45 + (0 * 20))

        chk_bln4[2] = tk.BooleanVar()
        chk_4[2] = tk.Checkbutton(frame4, variable=chk_bln4[2], text=chk_txt1[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[2].place(x=10, y=45 + (1 * 20))

        chk_bln4[3] = tk.BooleanVar()
        chk_4[3] = tk.Checkbutton(frame4, variable=chk_bln4[3], text=chk_txt1[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[3].place(x=10, y=45 + (2 * 20))

        # ラベルを作成
        self.label1_2 = tk.Label(frame4, text=u"シャツ類",font=("MSゴシック", "12", "bold"))
        self.label1_2.place(x=5,y=120)

        # 全選択ボタン
        all_select_4_2 = tk.Button(frame4, text='全選択', command=lambda:self.all2(4), width=6, height=1, font=("MSゴシック", "10"))
        all_select_4_2.place(x=85,y=117)

        # チェックボタンを配置
        chk_bln4[4] = tk.BooleanVar()
        chk_4[4] = tk.Checkbutton(frame4, variable=chk_bln4[4], text=chk_txt2[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[4].place(x=10, y=140 + (0 * 20))

        chk_bln4[5] = tk.BooleanVar()
        chk_4[5] = tk.Checkbutton(frame4, variable=chk_bln4[5], text=chk_txt2[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[5].place(x=10, y=140 + (1 * 20))

        chk_bln4[6] = tk.BooleanVar()
        chk_4[6] = tk.Checkbutton(frame4, variable=chk_bln4[6], text=chk_txt2[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[6].place(x=10, y=140 + (2 * 20))

        chk_bln4[7] = tk.BooleanVar()
        chk_4[7] = tk.Checkbutton(frame4, variable=chk_bln4[7], text=chk_txt2[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[7].place(x=10, y=140 + (3 * 20))

        chk_bln4[8] = tk.BooleanVar()
        chk_4[8] = tk.Checkbutton(frame4, variable=chk_bln4[8], text=chk_txt2[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[8].place(x=10, y=140 + (4 * 20))

        chk_bln4[9] = tk.BooleanVar()
        chk_4[9] = tk.Checkbutton(frame4, variable=chk_bln4[9], text=chk_txt2[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[9].place(x=120, y=140 + (4 * 20))

        chk_bln4[10] = tk.BooleanVar()
        chk_4[10] = tk.Checkbutton(frame4, variable=chk_bln4[10], text=chk_txt2[6], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[10].place(x=10, y=140 + (5 * 20))

        # ラベルを作成
        self.label1_3 = tk.Label(frame4, text=u"ズボン類",font=("MSゴシック", "12", "bold"))
        self.label1_3.place(x=5,y=272)

        # 全選択ボタン
        all_select_4_3 = tk.Button(frame4, text='全選択', command=lambda:self.all3(4), width=6, height=1, font=("MSゴシック", "10"))
        all_select_4_3.place(x=85,y=272)

        # チェックボタンを配置
        chk_bln4[11] = tk.BooleanVar()
        chk_4[11] = tk.Checkbutton(frame4, variable=chk_bln4[11], text=chk_txt3[0], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[11].place(x=10, y=295 + (0 * 20))

        chk_bln4[12] = tk.BooleanVar()
        chk_4[12] = tk.Checkbutton(frame4, variable=chk_bln4[12], text=chk_txt3[1], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[12].place(x=120, y=295 + (0 * 20))

        chk_bln4[13] = tk.BooleanVar()
        chk_4[13] = tk.Checkbutton(frame4, variable=chk_bln4[13], text=chk_txt3[2], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[13].place(x=10, y=295 + (1 * 20))

        chk_bln4[14] = tk.BooleanVar()
        chk_4[14] = tk.Checkbutton(frame4, variable=chk_bln4[14], text=chk_txt3[3], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[14].place(x=120, y=295 + (1 * 20))

        chk_bln4[15] = tk.BooleanVar()
        chk_4[15] = tk.Checkbutton(frame4, variable=chk_bln4[15], text=chk_txt3[4], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[15].place(x=10, y=295 + (2 * 20))

        chk_bln4[16] = tk.BooleanVar()
        chk_4[16] = tk.Checkbutton(frame4, variable=chk_bln4[16], text=chk_txt3[5], font=("MSゴシック", "10", "bold"), command=self.playSE_1) 
        chk_4[16].place(x=10, y=295 + (3 * 20))

        for i in range(len(cloth4)):
            if cloth4[i] == "1":
                chk_bln4[i].set(True)

    # 体感気温フレーム
    def frame5(self):

        global txt_box5
        txt_box5 = {}

        with open('UserData/temp.txt',encoding="utf-8") as f:
            self.UserTemp = f.readlines()
            for i in range(len(self.UserTemp)):
                self.UserTemp[i] = self.UserTemp[i].strip()

        # フレームの設定
        frame5 = ttk.Frame(root, width=400, height=200,relief=tk.RIDGE)
        frame5.place(anchor=tk.CENTER,x=225,y=550)

        # ラベルを作成
        self.label5_1 = tk.Label(frame5, text=u"体感気温の設定",font=("MSゴシック", "13", "bold"),bg="blue",foreground='#ffffff')
        self.label5_1.place(x=0,y=0,relwidth=1)

        # ラベルを作成
        self.label15_2 = tk.Label(frame5, text=u"あなたが暑く感じる気温は　　   ℃以上",font=("MSゴシック", "15", "bold"))
        self.label15_2.place(x=5,y=80)

        # テキストボックスを作成
        txt_box5[0] = tk.Entry(frame5, font=("MSゴシック", "20", "bold"),justify="center")
        txt_box5[0].place(anchor=tk.CENTER,x=290,y=80,width=50,height=50)
        txt_box5[0].insert(0, self.UserTemp[0])

        # ラベルを作成
        self.label15_3 = tk.Label(frame5, text=u"あなたが寒く感じる気温は　　   ℃以下",font=("MSゴシック", "15", "bold"))
        self.label15_3.place(x=5,y=160)

        # テキストボックスを作成
        txt_box5[1] = tk.Entry(frame5, font=("MSゴシック", "20", "bold"),justify="center")
        txt_box5[1].place(anchor=tk.CENTER,x=290,y=160,width=50,height=50)
        txt_box5[1].insert(0, self.UserTemp[1])


    # 着慣れている服の登録フレーム
    #def frame6(self):


def sub():
    global root
    global sub_flag
    sub_flag = 1
    root = tk.Tk()              # rootインスタンスを生成
    # 閉じるボタンの無効化
    root.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # 最大化の無効
    root.resizable(0, 0)
    f1 = SubWindow(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し

if __name__ == "__main__":      # このファイルが実行されている場合の処理
    global root
    global sub_flag
    sub_flag = 1
    root = tk.Tk()              # rootインスタンスを生成
    f1 = SubWindow(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し