# データセット作成プログラム（カラー画像バージョン）
import cv2
import random
import numpy as np
from PIL import Image
import os
import random

def read_image():

    # 設定パラメータ
    img_size = 50
    class_n = 2   # クラス数（服の週類の数）
    x = []        # 画像データ用
    y = []        # ラベルデータ用
    DIR = "mirror" # パス
    CATEGORIES = os.listdir(DIR)

    # ファイルの保存先を指定（ファイルの拡張子は.npz）
    outfile = str(img_size) + "px_" + str(class_n) +  ".npz"

    # path 以下の画像を読み込む
    def glob_files(path, label):

        # 各ファイルを処理
        fl = os.listdir(path)
        random.shuffle(fl)

        for f in fl:
            
            # 画像ファイルを読む
            img = cv2.imread(os.path.join(path, f))

            b, g, r = cv2.split(img)
            img = cv2.merge([r,g,b])

            img = np.asarray(img)  # ndarray化
            img = cv2.resize(img, (img_size, img_size), cv2.INTER_LANCZOS4)  # 画像サイズをimg_sizeに揃える
            
            # 画像データ(img)とラベルデータ(label)をx, y のそれぞれのリストに保存
            x.append(img)
            y.append(label)

    i = 0
    for i in range(class_n):
        glob_files(os.path.join(DIR, CATEGORIES[i]), i)  # 各画像のフォルダーを読む
        print("file: " + CATEGORIES[i])

    ### ファイルへ保存 ###
    # npzで作成する場合
    np.savez(outfile, x=x, y=y)
    print("npzファイルを保存しました :" + outfile, len(x))

#if __name__ == '__main__':
    #read_image()