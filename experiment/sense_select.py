# 服画像の分類
import cnn_model_s
import numpy as np
import cv2.cv2 as cv
import os

img_size = 50  # 画像サイズ
im_color = 3    # 画像の色空間
in_shape = (img_size, img_size, im_color)
num_classes = 2 # 分類数

#DIR = "fashion"
LABELS = ["好みに合わない","好みに合う"]

def answer(img1):

    # CNNモデルを取得  
    model = cnn_model_s.get_model(in_shape, num_classes)
    # 保存したモデルを読み込む
    model.load_weights(str(num_classes)+'.hdf5')

    # img1 = cv.imread(img1)
    img1 = cv.resize(img1,(img_size,img_size))   # サイズ変更

    # データに変換
    x = np.asarray(img1)
    x = x.reshape(-1, img_size, img_size, im_color)
    x = x / 255

    # 予測
    pre = model.predict([x])[0]
    idx = pre.argmax()
    per = pre[int(idx)] * 100

    # 分類結果の表示
    # print(idx)
    # print(pre)
    print("この写真は" + LABELS[int(idx)] + "　確率：" + str(int(per)) + "%")

    return idx


#if __name__ == "__main__":
    #i = answer("C:/Users/inuka/prototype/tekitou/sensegazou/kirai/6.png")
    #print("分類結果：" + LABELS[int(i)])