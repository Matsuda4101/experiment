# -*- coding: utf-8 -*-
# ↑これ書けば日本語使えるようになるよ
# 服画像分類プログラム
import cnn_model_c
import numpy as np
import cv2.cv2 as cv

im_rows = 50   # 画像の縦ピクセルサイズ
im_cols = 50   # 画像の横ピクセルサイズ
im_color = 3    # 画像の色空間
in_shape = (im_rows, im_cols, im_color)
num_classes = 15 # 分類数

DIR = "CNN/photo_storage"
LABELS = ["長袖ボタンシャツ","半袖ボタンシャツ","チノパン","コート","ハーフパンツ","ジャケット","ジーパン","パーカー","ポロシャツ","ショートパンツ","スラックス","スウェット","セーター","半袖Tシャツ","長袖Tシャツ"]

# CNNモデルを取得  
model = cnn_model_c.get_model(in_shape, num_classes)
# 保存したモデルを読み込む
model.load_weights(str(num_classes)+'.hdf5')

def answer(img_path):

    # 画像を読み込む
    img = cv.imread(img_path)
    img1 = cv.resize(img,(im_cols,im_rows))   # サイズ変更

    # データに変換
    x = np.asarray(img1)
    x = x.reshape(-1, im_rows, im_cols, im_color)
    x = x / 255

    # 予測
    pre = model.predict([x])[0]
    idx = pre.argmax()
    per = pre[idx] * 100

    # print(pre)
    # print("この写真が", LABELS[idx], "である可能性は", per, "%")
    # print("この画像は"+LABELS[idx]+"で合っていますか？[y/n]")

    # 分類結果を返す
    return LABELS[idx]


# 単体で動かすときだけ下3行は必要
# 他プログラムから呼び出すときはこっから下はコメントアウトして
#if __name__ == '__main__':
    #s = answer("ここに画像のパス")  # sに返り値が入る
   # print(s)

