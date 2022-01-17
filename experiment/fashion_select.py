# 服画像の分類
import cnn_model_f
import numpy as np
import cv2.cv2 as cv
from PIL import Image
import os

img_size = 50  # 画像サイズ
im_color = 3    # 画像の色空間
in_shape = (img_size, img_size, im_color)
num_classes = 3 # 分類数

#DIR = "fashion"
LABELS = ["派手","シンプル","暗め"]

# CNNモデルを取得  
model = cnn_model_f.get_model(in_shape, num_classes)
# 保存したモデルを読み込む
model.load_weights(str(num_classes)+'.hdf5')

def answer(fashion,img):
    img1 = cv.resize(img,(img_size,img_size))   # サイズ変更

    # データに変換
    x = np.asarray(img1)
    x = x.reshape(-1, img_size, img_size, im_color)
    x = x / 255

    # 予測
    pre = model.predict([x])[0]
    idx = pre.argmax()
    per = pre[int(fashion)] * 100

    # 分類結果の表示
    print(pre)
    print("この写真が", LABELS[int(fashion)], "である可能性は", per, "%")

    return idx, per