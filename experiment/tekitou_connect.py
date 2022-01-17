import cv2

# 引数の画像同士を結合する
def get_concat_v(image1_path,image2_path,image3_path):
  # パスから画像を開く
  image1 = cv2.imread(image1_path)
  #image1 = grabcut.grabCutFirst(image1) # 背景の除去
  # 画像をリサイズ（幅300に固定、高さもそれに比例）
  height1, width1 = image1.shape[:2]
  image1 = cv2.resize(image1, dsize=(300, int(height1*(300/width1))))
  #cv2.imshow("kiseta!",image1)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()

  # 画像をリサイズ（幅300に固定、高さもそれに比例）
  image2 = cv2.imread(image2_path)
  #image2 = grabcut.grabCutFirst(image2) # 背景の除去
  height2, width2 = image2.shape[:2]
  image2 = cv2.resize(image2, dsize=(300, int(height2*(300/width2))))
  #cv2.imshow("kiseta",image2)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()
  # 上下画像を結合
  dst = cv2.vconcat([image1, image2])

  # 上着がある場合着せる
  if image3_path != 0:
    image3 = cv2.imread(image3_path)
    #image3 = grabcut.grabCutFirst(image3) # 背景の除去
    height3, width3 = image3.shape[:2]
    image3 = cv2.resize(image3, dsize=(300, int(height3*(300/width3))))

    # 上着を左右でトリミング（img[top : bottom, left : right]）
    img1 = image3[0 : int(height3*(300/width3)), 0: 100]
    img2 = image3[0 : int(height3*(300/width3)), 200 : 300]

    # 上着をdstに結合
    dst[0 : int(height3*(300/width3)), 0: 100] = img1
    dst[0 : int(height3*(300/width3)), 200 : 300] = img2

  else:
    image3 = []

  # cv2.imshow("kiseta!",dst)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  
  return image1, image2, image3, dst