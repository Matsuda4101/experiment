# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import cv2
import numpy as np
import os

# 画像のトリミング
def crop_center(pil_img):
    img_height, img_width = pil_img.shape[:2]
    img1 = pil_img[int(img_height/4):int((img_height*3)/4) , int(img_width/4):int((img_width*3)/4)]
    return img1

def color_get(file_path,c):

    box = []

    for f in os.listdir(file_path):

        max_color=0
        max_code=0

        # 画像の取得
        img_path = os.path.join(file_path,f)
        img = cv2.imread(img_path)

        # 画像サイズの50%で中心部をトリミング
        image = crop_center(img)
        #cv2.imshow("gray",image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # こっから色彩抽出
        # K-means法でクラスタリング（メインカラー4色に分類）
        image = image.reshape((image.shape[0] * image.shape[1], 3))
        clt = KMeans(n_clusters = 3)
        clt.fit(image)

        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=numLabels)

        hist = hist.astype("float")
        hist /= hist.sum()

        bar = np.zeros((50, 300, 3), dtype="uint8")
        cluster_centers_arr = clt.cluster_centers_.astype(int, copy=False)
        startX = 0

        # 最も割合の多い色を抽出
        for (percent, color) in zip(hist, cluster_centers_arr):
            color_hex_str = '#%02x%02x%02x' % tuple(color)
            #print(percent , color_hex_str)
            if max_color < percent:
                max_color = percent
                max_code = color_hex_str
            endX = startX + (percent * 300)
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),color.astype("uint8").tolist(), -1)
            startX = endX
        
        # カラーコードをRGB変換
        color_code = (int(max_code[1:3],16),int(max_code[3:5],16),int(max_code[5:7],16))
        # print("メインカラー：",max_color,color_code)

        r,g,b = color_code
        flag = color_check(c,r,g,b)

        if flag == 1:
            box.append(img_path)
    return box


def color_check(color,r,g,b):
    if color == "赤":
        if r > 100 and abs(g-b) < 40 and (g < r - 100 or b < r - 100):
            return 1
        else:
            return 0

    elif color == "黄":
        if r > 180 and g > 180 and (b < r - 80 or b < g - 80) and r > g:
            return 1
        else:
            return 0

    elif color == "青":
        if (b > g and r < g - 20) or (r < g and b > g + 30):
            return 1
        else:
            return 0

    elif color == "緑":
        if (g < 150 and r < g and b < g and (r < g - 20 or b < g - 20)) or (g >= 150 and abs(r-b) < 100 and r < g - 20 and b < g - 20) :
            return 1
        else:
            return 0

    elif color == "黒":
        if r < 80 and g < 80 and b < 80 and abs(r-b) < 15 and abs(g-b) < 15 and abs(b-g) < 15:
            return 1
        else:
            return 0

    elif color == "白":
        if r >= 220 and g >= 220 and b >= 220 and abs(r-b) < 20 and abs(g-b) < 20 and abs(b-g) < 20:
            return 1
        else:
            return 0

#if __name__ == '__main__':
    #b = color_get("photo_storage/buttonshirt_L","白")
    #print(b)