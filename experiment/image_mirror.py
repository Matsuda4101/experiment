# OpenCVの簡単な例
import cv2.cv2 as cv
import os

def mirror(path,num):
    j = len(os.listdir(path))+1
    k = j
    for i in range(1, k):
        img = cv.imread(path + "/" + str(i) + ".png")
        img1 = cv.flip(img, 1)

        if num == 0:
            cv.imwrite('mirror/like/' + str(i) + ".png", img)
            cv.imwrite('mirror/like/' + str(j) + ".png", img1)
        elif num == 1:
            cv.imwrite('mirror/dislike/' + str(i) + ".png", img)
            cv.imwrite('mirror/dislike/' + str(j) + ".png", img1)
        j = j + 1