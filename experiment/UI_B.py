# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
from pygame import mixer
from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import cv2
import os

import choice_B
import weather
import setting
import maingamen

# tk.Frameを継承したFrame1クラスを作成
class Frame1(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=1600, height=900) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定
 
        # 画面の真ん中に表示？
        window_width= 1600
        window_height= 900
        a= int(int(root.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root.winfo_screenheight()/2) -int(window_height/2))
        root.geometry(f"{window_width}x{window_height}+{a}+{b}")

        #ウィンドウの設定
        self.master.title("自称オートコーディネートシステム")

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"あなたに合ったコーデ作ります！",font=("MSゴシック", "20", "bold"),bg="blue",foreground='#ffffff')
        self.label1.pack(fill=tk.X)

        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # 戻るボタン作成 
        btn1 = tk.Button(root, text='戻る', width=10, height=2, command=self.re_main, font=("MSゴシック", "10"))
        btn1.place(anchor=tk.CENTER,x=70,y=770)

        # 絞り込み条件の変更ボタンの作成 
        btn2 = tk.Button(root, text='設定', command=self.sub_window, width=10, height=2, font=("MSゴシック", "10"))
        btn2.place(anchor=tk.CENTER,x=180,y=770)

        # 各種フレーム・ボタン等を配置
        self.set_frame1()
        self.set_frame2()
        #self.set_frame3()
        #self.set_frame4("Nigata")

    # タイトル画面に戻る
    def re_main(self):
        self.playSE_1()
        root.destroy()
        maingamen.modoru()

    # 決定ボタンクリックイベント
    def btn_click(self, btn):
        global label3

        self.playSE_1()
        
        # 決定ボタンを非表示・待機文表示
        btn.destroy()
        label3 = tk.Label(frame1, text=u"コーデ出力中\nしばらくお待ちください",font=("MSゴシック", "15", "bold"))
        label3.place(anchor=tk.CENTER,x=150,y=590)

        # 0.001秒後に関数呼び出し
        root.after(10, self.get_corde)

    # 各服画像の取得・表示
    def get_corde(self):

        favorite_flag = 0
        # 3分クッキングBGM
        self.playBGM()

        global save

        self.num1 = rdo_var.get()
        self.num2 = rdo_var2.get()
        self.num3 = rdo_var3.get()
        self.num4 = combobox.get()

        if self.num4 == "北海道":
            self.num4 = "Hokkaido"
        elif self.num4 == "東京":
            self.num4 = "Tokyo"
        elif self.num4 == "広島":
            self.num4 = "Hiroshima"
        elif self.num4 == "大阪":
            self.num4 = "Osaka"
        elif self.num4 == "沖縄":
            self.num4 = "Okinawa"            

        #print(self.num4)
        self.corde, self.up, self.down, self.outer, save= choice_B.nice_fashion(rdo_txt[self.num1], rdo_txt2[self.num2], self.num3, self.num4 )

        # 各画像を出力
        self.img_show(self.corde, self.up, self.down, self.outer)
        label3['text'] = '出力完了'
        self.playSE_3()
        #self.stopBGM()

        # 質問を表示
        self.set_frame3()
        self.set_frame4(self.num4)

    # ここでコーデを表示
    def img_show(self, corde, up, down, outer):
        self.corde = corde
        self.up = up
        self.down = down
        self.outer = outer

        # コーデ画像をcanvasに合うようにリサイズ
        self.height, self.width = self.corde.shape[:2]
        self.corde = cv2.resize(self.corde, dsize=(int(self.width*(600/self.height)), 600))
        self.corde1 = self.cv_to_pil(self.corde)
        # コーデ画像をcanvasに表示
        canvas1.create_image(175, 322, image=self.corde1, anchor='center')

        # 上画像をcanvasに合うようにリサイズ
        self.height, self.width = self.up.shape[:2]
        self.up = cv2.resize(self.up, dsize=(int(self.width*(160/self.height)), 160))
        self.up1 = self.cv_to_pil(self.up)
        # 上画像をcanvasに表示
        canvas2.create_image(175, 90, image=self.up1, anchor='center')

        # 下画像をcanvasに合うようにリサイズ
        self.height, self.width = self.down.shape[:2]
        self.down = cv2.resize(self.down, dsize=(int(self.width*(160/self.height)), 160))
        self.down1 = self.cv_to_pil(self.down)
        # 下画像をcanvasに表示
        canvas3.create_image(175, 90, image=self.down1, anchor='center')

        # 上着があるか判定
        if len(self.outer) != 0:
            # 上着画像をcanvasに合うようにリサイズ
            self.height, self.width = self.outer.shape[:2]
            self.outer = cv2.resize(self.outer, dsize=(int(self.width*(160/self.height)), 160))
            self.outer1 = self.cv_to_pil(self.outer)
            # 上着画像をcanvasに表示
            canvas4.create_image(175, 90, image=self.outer1, anchor='center')
        # 無い場合「No item」と表示
        else:
            canvas4.create_text(175,90 ,text="No item", font=("Helvetica", 40, "bold"))

    # フォーマット変換
    def cv_to_pil(self, img):
        self.img = img
        self.image_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # imreadはBGRなのでRGBに変換
        self.image_pil = Image.fromarray(self.image_rgb)            # RGBからPILフォーマットへ変換
        self.image_tk  = ImageTk.PhotoImage(self.image_pil)         # ImageTkフォーマットへ変換
        return self.image_tk

    # 「予定」のラジオボタンを操作した場合
    #def plan(self):
        #self.playSE_1()
        #self.num = rdo_var.get()
        #if self.num == 3:
            #combobox.configure(state="readonly")
        #else:
            #combobox.configure(state="disable")
    
    # 「気に入らない」のラジオボタンを操作した場合
    def prefer(self):
        self.playSE_1()
        self.num = rdo_var4.get()
        if self.num == 1:
            chk_0.configure(state="disable")
            chk_1.configure(state="disable")
            chk_2.configure(state="disable")
            chk_3.configure(state="normal")
            chk_4.configure(state="normal")
            chk_5.configure(state="normal")
        else:
            chk_0.configure(state="normal")
            chk_1.configure(state="normal")
            chk_2.configure(state="normal")
            chk_3.configure(state="disable")
            chk_4.configure(state="disable")
            chk_5.configure(state="disable")

    # 「回答」ボタンクリックイベント
    def reset(self):
        self.playSE_4()

        #入力データを保存
        self.save_img()
        #self.save_txt()

        tk.messagebox.showinfo('回答完了', '回答内容を保存しました')

        # 各状態をリセット
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        frame4.destroy()

        self.set_frame1()
        self.set_frame2()
        #self.set_frame3()

    # 出力画像を保存する
    def save_img(self):
        l1 = ["office","shop","home","trip"]
        l2 = ["red","blue","yellow","green","white","black","no"]
        l3 = ["hade","simple","dark"]

        num1 = rdo_var4.get()
        num2 = rdo_var.get()
        num3 = rdo_var2.get()
        num4 = rdo_var3.get()

        if num1 == 0:
            # 気に入らない場合
            if chk_bln1[0].get() == 1:
                self.a = 1
            else:
                self.a = 0
            if chk_bln1[1].get() == 1:
                self.b = 1
            else:
                self.b = 0
            if chk_bln1[2].get() == 1:
                self.c = 1
            else:
                self.c = 0

            files = len(os.listdir("prefer/like"))+1
            cv2.imwrite("prefer/like/"+ str(self.a) + str(self.b) + str(self.c) + "_" + l1[num2] + "_" + l2[num3] + "_" + l3[num4] + "_" + str(int(temp)) + "_" + str(files) +".png",save)
        else:
            # 気に入らない場合
            if chk_bln2[0].get() == 1:
                self.a = 1
            else:
                self.a = 0
            if chk_bln2[1].get() == 1:
                self.b = 1
            else:
                self.b = 0
            if chk_bln2[2].get() == 1:
                self.c = 1
            else:
                self.c = 0
            files = len(os.listdir("prefer/dislike"))+1
            cv2.imwrite("prefer/dislike/"+ str(self.a) + str(self.b) + str(self.c) + "_" + l1[num2] + "_" + l2[num3] + "_" + l3[num4] + "_" + str(int(temp)) + "_" + str(files) +".png",save)
        print("保存完了")
    
    # 服装基準（お客さんの入力データ）を保存する
    #def save_txt(self):
        #for i in range(len(chk_bln3)):
            #num = chk_bln3[i].get()
            #if num == 1:
                #with open('question/data.txt') as f:
                    #lines = f.readlines()

                #with open('question/data.txt', mode='w') as f:
                    #lines[i] = str(int(lines[i]) + 1) + "\n"
                    #f.writelines(lines)

                # 「その他」の場合は回答文を保存
                #if i == 6:
                    #ith open('question/other.txt', mode='a') as f:
                        #f.write(txt_box.get() + "\n")

    # 「その他」を押した場合のテキストボックス表示・非表示
    #def other(self,num):
        #global txt_flag
        #self.playSE_1()

        #self.num = num
        #if self.num == 6:
            #if txt_flag == 0:
                #txt_box.configure(state="normal")
                #txt_flag = 1
            #else:
                #txt_box.configure(state="disable")
                #txt_flag = 0
    
    # 設定ボタン
    def sub_window(self):
        self.playSE_1()
        root.destroy()
        setting.sub()        

    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)
    
    def playSE_2(self,event):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)
    
    def playSE_3(self):
        mixer.init()
        mixer.music.load("SE/niku.mp3")
        mixer.music.play(1)

    def playSE_4(self):
        mixer.init()
        mixer.music.load("SE/don.mp3")
        mixer.music.play(1)

    def playBGM(self):
        mixer.init()
        mixer.music.load("SE/minutes.mp3")
        mixer.music.play(-1)

    def stopBGM(self):
        mixer.music.stop()


    def set_frame1(self):
        global frame1

        # フレームの設定
        frame1 = ttk.Frame(root, width=300, height=650,relief=tk.RIDGE)
        frame1.place(x=30,y=80)

        # 予定データを読み込む
        with open('UserData/plan.txt',encoding="utf-8") as f:
            self.lines = f.readlines()
            for i in range(len(self.lines)):
                self.lines[i] = self.lines[i].strip()            
            #print(self.lines)
            
        # ラジオボタンのラベルをリスト化する
        global rdo_txt
        rdo_txt = self.lines
        global rdo_txt2
        rdo_txt2 = ['赤','青','黄','緑','白','黒','no']
        global rdo_txt3
        rdo_txt3 = ['派手','シンプル','ダーク']

        # ラジオボタンの状態
        global rdo_var
        rdo_var = tk.IntVar()
        global rdo_var2
        rdo_var2 = tk.IntVar()
        global rdo_var3
        rdo_var3 = tk.IntVar()

        # コンボボックスの設定
        global combobox
        c_text = ["北海道","大阪","東京","広島","沖縄"]

        # ラベルを作成
        self.label2 = tk.Label(frame1, text=u"本日の予定を入力してください",font=("MSゴシック", "13", "bold"),bg="blue",foreground='#ffffff')
        self.label2.place(x=0,y=0,relwidth=1)

        # ラジオボタンを作成
        rdo1 = tk.Radiobutton(frame1, value=0, variable=rdo_var, text=rdo_txt[0], command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
        rdo1.place(x=20,y=35)

        rdo2 = tk.Radiobutton(frame1, value=1, variable=rdo_var, text=rdo_txt[1], command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
        rdo2.place(x=20,y=65)

        rdo3 = tk.Radiobutton(frame1, value=2, variable=rdo_var, text=rdo_txt[2], command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
        rdo3.place(x=20,y=95)

        rdo4 = tk.Radiobutton(frame1, value=3, variable=rdo_var, text=rdo_txt[3], command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
        rdo4.place(x=20,y=125)


        # ラベルを作成
        self.label5 = tk.Label(frame1, text=u"目的地",font=("MSゴシック", "13", "bold"))
        self.label5.place(x=200,y=70)
        
        # コンボボックスを作成
        combobox = ttk.Combobox(frame1,height=5,values=c_text, justify="center", state="readonly", font=("MSゴシック", "12", "bold"))
        combobox.bind("<<ComboboxSelected>>",self.playSE_2)
        combobox.set("東京")
        combobox.place(x=202,y=95,width=80,height=25)

        # ラベルを作成
        self.label3 = tk.Label(frame1, text=u"好きな色を入力してください",font=("MSゴシック", "13", "bold"),bg="blue",foreground='#ffffff')
        self.label3.place(x=0,y=170,relwidth=1)
        # ラジオボタンを動的に作成
        for i in range(len(rdo_txt2)-1):
            rdo2 = tk.Radiobutton(frame1, value=i, variable=rdo_var2, text=rdo_txt2[i], command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
            rdo2.place(x=20,y=205+(i*30))
        
        rdo2 = tk.Radiobutton(frame1, value=6, variable=rdo_var2, text="指定なし", command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
        rdo2.place(x=150,y=205)

        # ラベルを作成
        self.label4 = tk.Label(frame1, text=u"好きな見た目を入力してください",font=("MSゴシック", "13", "bold"),bg="blue",foreground='#ffffff')
        self.label4.place(x=0,y=410,relwidth=1)
        # ラジオボタンを動的に作成
        for i in range(len(rdo_txt3)):
            rdo3 = tk.Radiobutton(frame1, value=i, variable=rdo_var3, text=rdo_txt3[i], command=self.playSE_1, font=("MSゴシック", "15", "bold")) 
            rdo3.place(x=20,y=445+(i*30))

        # 決定ボタン作成 
        btn1 = tk.Button(frame1, text='決定', command=lambda:self.btn_click(btn1), width=12, height=2, font=("MSゴシック", "20"))
        btn1.place(anchor=tk.CENTER,x=150,y=590)
     
    def set_frame2(self):
        global frame2

        global c_frame1
        global c_frame2
        global c_frame3
        global c_frame4
        global c_frame5

        global canvas1
        global canvas2
        global canvas3
        global canvas4

        # フレームの作成
        frame2 = tk.Frame(root, width=800, height=700, bg="whitesmoke")
        frame2.place(anchor=tk.CENTER,x=760,y=460)
        frame2.propagate(False)

        c_frame1 = tk.Frame(frame2, width=400, height=700, bg="whitesmoke")
        c_frame1.pack(side=tk.LEFT,padx=5)
        c_frame1.propagate(False)

        c_frame2 = tk.Frame(frame2, width=400, height=700, bg="whitesmoke")
        c_frame2.pack(side=tk.RIGHT,padx=5)
        c_frame2.propagate(False)

        c_frame3 = tk.Frame(c_frame2, width=400, height=233, bg="whitesmoke")
        c_frame3.pack()
        c_frame3.propagate(False)

        c_frame4 = tk.Frame(c_frame2, width=400, height=233, bg="whitesmoke")
        c_frame4.pack()
        c_frame4.propagate(False)

        c_frame5 = tk.Frame(c_frame2, width=400, height=234, bg="whitesmoke")
        c_frame5.pack()
        c_frame5.propagate(False)

        # キャンバスの設定
        canvas1 = tk.Canvas(c_frame1, width=350, height=645, bg="white")
        canvas1.pack(side=tk.BOTTOM, pady=10)
        canvas1.create_rectangle(3, 3, 350, 645,fill="white",width=3,outline="#a9a9a9")

        canvas2 = tk.Canvas(c_frame3, width=350, height=180, bg="white")
        canvas2.pack(side=tk.BOTTOM, pady=10)
        canvas2.create_rectangle(3, 3, 350, 180,fill="white",width=3,outline="#a9a9a9")

        canvas3 = tk.Canvas(c_frame4, width=350, height=180, bg="white")
        canvas3.pack(side=tk.BOTTOM, pady=10)
        canvas3.create_rectangle(3, 3, 350, 180,fill="white",width=3,outline="#a9a9a9")

        canvas4 = tk.Canvas(c_frame5, width=350, height=180, bg="white")
        canvas4.pack(side=tk.BOTTOM, pady=10)
        canvas4.create_rectangle(3, 3, 350, 180,fill="white",width=3,outline="#a9a9a9")

        # ラベルを作成
        self.c_label1 = tk.Label(c_frame1, text=u"全体",font=("MSゴシック", "20", "bold"), bg="whitesmoke")
        self.c_label1.pack()

        self.c_label2 = tk.Label(c_frame3, text=u"上",font=("MSゴシック", "20", "bold"), bg="whitesmoke")
        self.c_label2.pack()

        self.c_label3 = tk.Label(c_frame4, text=u"下",font=("MSゴシック", "20", "bold"), bg="whitesmoke")
        self.c_label3.pack()
        
        self.c_label4 = tk.Label(c_frame5, text=u"上着",font=("MSゴシック", "20", "bold"), bg="whitesmoke")
        self.c_label4.pack()

    def set_frame3(self):
        # グローバル変数宣言
        global frame3

        global rdo_txt4
        global rdo_var4

        global chk_bln1
        global chk_bln2
        global chk_bln3
        global chk_txt1
        global chk_txt2
        global chk_txt3

        global chk_0
        global chk_1
        global chk_2
        global chk_3
        global chk_4
        global chk_5

        global txt_box
        global txt_flag

        txt_flag = 0

        frame3 = ttk.Frame(root, width=300, height=650,relief=tk.RIDGE)
        frame3.place(x=1200,y=80)    

        # ラベルを作成
        self.label2 = tk.Label(frame3, text=u"出力結果を気に入りましたか？",font=("MSゴシック", "12", "bold"),bg="blue",foreground='#ffffff')
        self.label2.place(x=0,y=0,relwidth=1)

        # ラジオボタンのラベルをリスト化する
        rdo_txt4 = ['気に入った！','気に入らない...']

        # ラジオボタンの状態
        rdo_var4 = tk.IntVar()

        # ラジオボタンを作成（気に入った）
        rdo = tk.Radiobutton(frame3, value=0, variable=rdo_var4, text=rdo_txt4[0], command=self.prefer, font=("MSゴシック", "15", "bold")) 
        rdo.place(x=40,y=35)

        # チェックボタンのラベルをリスト化する
        chk_txt1 = ["色合いが良い","気温と合っている","予定と合っている"]
        # チェックボックスON/OFFの状態
        chk_bln1 = {}

        # チェックボタンを動的に配置
        chk_bln1[0] = tk.BooleanVar()
        chk_0 = tk.Checkbutton(frame3, variable=chk_bln1[0], text=chk_txt1[0], font=("MSゴシック", "13", "bold"), command=self.playSE_1) 
        chk_0.place(x=60, y=65 + (0 * 25))

        chk_bln1[1] = tk.BooleanVar()
        chk_1 = tk.Checkbutton(frame3, variable=chk_bln1[1], text=chk_txt1[1], font=("MSゴシック", "13", "bold"), command=self.playSE_1) 
        chk_1.place(x=60, y=65 + (1 * 25))

        chk_bln1[2] = tk.BooleanVar()
        chk_2 = tk.Checkbutton(frame3, variable=chk_bln1[2], text=chk_txt1[2], font=("MSゴシック", "13", "bold"), command=self.playSE_1) 
        chk_2.place(x=60, y=65 + (2 * 25))


        # ラジオボタンを作成（気に入らない）
        rdo = tk.Radiobutton(frame3, value=1, variable=rdo_var4, text=rdo_txt4[1], command=self.prefer, font=("MSゴシック", "15", "bold")) 
        rdo.place(x=40,y=145)

        # チェックボタンのラベルをリスト化する
        chk_txt2 = ["色合いが悪い\n（好みではない）","気温と合っていない","予定と合っていない"]
        # チェックボックスON/OFFの状態
        chk_bln2 = {}

        # チェックボタンを動的に配置
        chk_bln2[0] = tk.BooleanVar()
        chk_3 = tk.Checkbutton(frame3, variable=chk_bln2[0], text=chk_txt2[0], state="disable", font=("MSゴシック", "13", "bold"), command=self.playSE_1) 
        chk_3.place(x=60, y=175 + (0 * 25))

        chk_bln2[1] = tk.BooleanVar()
        chk_4 = tk.Checkbutton(frame3, variable=chk_bln2[1], text=chk_txt2[1], state="disable", font=("MSゴシック", "13", "bold"), command=self.playSE_1) 
        chk_4.place(x=60, y=175 + (2 * 25))

        chk_bln2[2] = tk.BooleanVar()
        chk_5 = tk.Checkbutton(frame3, variable=chk_bln2[2], text=chk_txt2[2], state="disable", font=("MSゴシック", "13", "bold"), command=self.playSE_1) 
        chk_5.place(x=60, y=175 + (3 * 25))

        # 回答ボタン作成 
        btn2 = tk.Button(frame3, text='回答', command=self.reset, width=12, height=2, font=("MSゴシック", "20"))
        btn2.place(anchor=tk.CENTER,x=150,y=580)
    
    def set_frame4(self,place):

        self.place = place

        global canvas5
        global frame4
        global temp

        # フレームの作成
        frame4 = tk.Frame(root, width=330, height=50, bg="whitesmoke")
        frame4.place(anchor=tk.CENTER,x=760,y=75)
        frame4.propagate(False)

        # ラベルを作成
        self.label1 = tk.Label(frame4, text=combobox.get()+"の天気",font=("MSゴシック", "25", "bold"), bg="whitesmoke")
        self.label1.pack(side=tk.LEFT,padx=2)

        # 天気情報の取得
        temp, self.weather = weather.weather_get(self.place)

        canvas5 = tk.Canvas(frame4, width=50, height=50)
        canvas5.pack(side=tk.LEFT,padx=2)

        # 天気画像の貼り付け
        self.weather = cv2.resize(self.weather, dsize=(50,50))
        self.weather = self.cv_to_pil(self.weather)
        canvas5.create_image(25, 25, image=self.weather, anchor='center')

        # ラベルを作成
        self.label2 = tk.Label(frame4, text=str(str(int(temp))+"℃"),font=("MSゴシック", "25", "bold"), bg="whitesmoke")
        self.label2.pack(side=tk.LEFT,padx=2)


def corde():
    global root
    global sub_flag
    sub_flag = 0
    root = tk.Tk()              # rootインスタンスを生成
    #root.state('zoomed')
    # 画面の真ん中に表示？
    # 最大化の無効
    root.resizable(0, 0)
    f1 = Frame1(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し

if __name__ == "__main__":      # このファイルが実行されている場合の処理
    global sub_flag
    global root
    sub_flag = 0
    root = tk.Tk()              # rootインスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1 = Frame1(master=root)    # Frame1クラスからf1インスタンスを生成
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し