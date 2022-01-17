import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer
import cv2
from PIL import Image, ImageTk
import os
import tkinter.messagebox

import make_dataset
import image_learning
import t_fashion
import tekitou_connect
import image_mirror
import maingamen


 # tk.Frameを継承したFrame1クラスを作成
class Frame1(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=900, height=800) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        # 画面の真ん中に表示？
        window_width= 900
        window_height= 800
        a= int(int(root.winfo_screenwidth()/2) -int(window_width/2))
        b= int(int(root.winfo_screenheight()/2) -int(window_height/2))
        root.geometry(f"{window_width}x{window_height}+{a}+{b}")
 
        # グローバル変数を定義
        global canvas
        global flag
        global id
        global num
        num = 0

        flag = 0

        #ウィンドウの設定
        self.master.title("好みを覚えさせましょう")
 
        # フレームの設定
        self.config(bg="whitesmoke")    # 背景色を指定
        self.propagate(False)           # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack()             # フレームを配置

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"　　　出力結果が好きか嫌いか教えてください！",font=("MSゴシック", "20", "bold"),bg="blue",foreground='#ffffff')
        self.label1.pack(fill=tk.X)

        # キャンバスの設定
        canvas = tk.Canvas(self, width=800, height=550, bg="white") # Canvas作成
        canvas.place(anchor=tk.CENTER,x = 450,y = 320)

        self.btn_click()

        self.frame()    # ボタン配置

    def playSE_1(self):
        mixer.init()
        mixer.music.load("SE/click.mp3")
        mixer.music.play(1)

    # ボタンクリック時
    def btn_click(self):

        # グローバル変数を定義
        global canvas
        global flag
        global id
        global num

        if flag == 1:
            root.after_cancel(id)

        flag = 1        
        
        # 適当に服画像を抽出
        self.up, self.down, self.outer = t_fashion.tekitou()
        #print(self.up)
        #print(self.down)
        #print(self.outer)
        # 結合
        self.up, self.down, self.outer, self.corde = tekitou_connect.get_concat_v(self.up,self.down,self.outer)

        # print(self.corde.shape)
        self.height, self.width = self.corde.shape[:2]

        # コーデ画像をcanvasに合うようにリサイズ
        self.corde = cv2.resize(self.corde, dsize=(int(self.width*(550/self.height)), 550))
        self.corde1 = self.cv_to_pil(self.corde)

        # canvasに表示
        canvas.create_image(400, 275, image=self.corde1, anchor='center', tag="tekitou")

    
    def suki(self):
        self.playSE_1()

        files = len(os.listdir("learning_prefer_image/like"))+1

        self.a = len(os.listdir("learning_prefer_image/like"))
        #print(self.b)
        if self.a < 100:
            cv2.imwrite("learning_prefer_image/like/"+ str(files) +".png",self.corde)

        self.learn_button()
        self.btn_click()

    def kirai(self):
        self.playSE_1()
        
        files = len(os.listdir("learning_prefer_image/dislike"))+1

        self.b = len(os.listdir("learning_prefer_image/dislike"))
        #print(self.b)
        if self.b < 100:
            cv2.imwrite("learning_prefer_image/dislike/"+ str(files) +".png",self.corde)
        
        self.learn_button()
        self.btn_click()

    # 学習ボタンの無効有効
    def learn_button(self):

        # 分類画像が十分あるか確認
        self.a = len(os.listdir("learning_prefer_image/like"))
        #print(self.a)
        self.b = len(os.listdir("learning_prefer_image/dislike"))
        #print(self.b)
        if self.a >= 50 and self.b >= 50:
            button3.configure(state="normal")
        else:
            button3.configure(state="disable")

    # フォーマット変換
    def cv_to_pil(self, img):
        self.img = img
        self.image_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # imreadはBGRなのでRGBに変換
        self.image_pil = Image.fromarray(self.image_rgb)            # RGBからPILフォーマットへ変換
        self.image_tk  = ImageTk.PhotoImage(self.image_pil)         # ImageTkフォーマットへ変換
        return self.image_tk

    # 機械学習
    def learn(self):
        self.playSE_1()

        button3.configure(text="学習中...")
        root.after(1, self.learn_do)

    def learn_do(self):
        # ミラー画像の作成
        image_mirror.mirror("learning_prefer_image/like", 0)
        image_mirror.mirror("learning_prefer_image/dislike", 1)

        # データセットの作成
        make_dataset.read_image()

        #機械学習の実行
        image_learning.make_model()

        #学習終了後初期状態に戻る
        frame.destroy()
        self.frame()
        tk.messagebox.showinfo('正常終了', '学習が完了しました')

    def re(self):
        self.playSE_1()
        root.destroy()
        maingamen.modoru()

    def frame(self):
        global frame
        global button3

        frame = tk.Frame(root, width=400, height=180, bg="whitesmoke")
        frame.place(anchor=tk.CENTER,x=450, y=685)

        self.button1 = tk.Button(frame, text=u"好き！", command=self.suki, font=("MSゴシック", "20", "bold"), foreground="red")
        self.button1.place(anchor=tk.CENTER,x=100,y=50,width=150,height=75)

        self.button2 = tk.Button(frame, text=u"嫌い！", command=self.kirai, font=("MSゴシック", "20", "bold"), foreground="blue")
        self.button2.place(anchor=tk.CENTER,x=300,y=50,width=150,height=75)

        button3 = tk.Button(frame, text=u"学習させる", command=self.learn, font=("MSゴシック", "25", "bold"))
        button3.place(anchor=tk.CENTER,x=200,y=140,width=350,height=75)

        button4 = tk.Button(self, text=u"戻る", command=self.re, font=("MSゴシック", "20", "bold"))
        button4.place(x=50,y=710,width=120,height=70)

        self.learn_button()

 
def prefer():      # このファイルが実行されている場合の処理
    global root
    root = tk.Tk()              # rootインスタンスを生成
    f1 = Frame1(master=root)    # Frame1クラスからf1インスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し

if __name__ == "__main__":      # このファイルが実行されている場合の処理
    root = tk.Tk()              # rootインスタンスを生成
    f1 = Frame1(master=root)    # Frame1クラスからf1インスタンスを生成
    #root.state('zoomed')
    # 最大化の無効
    root.resizable(0, 0)
    f1.mainloop()               # f1インスタンスのイベントハンドラを呼び出し