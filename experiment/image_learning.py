# 学習モデルの作成
import cnn_model_s
from tensorflow import keras
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

im_rows = 50   # 画像の縦サイズ（ピクセル）
im_cols = 50   # 画像の横サイズ（ピクセル）
im_color = 3    # 画像の色空間
in_shape = (im_rows, im_cols, im_color)
num_classes = 2 # 分類数

def make_model():

    # 写真データを読み込み
    fashion_photos = np.load(str(im_cols)+"px_"+str(num_classes)+".npz")
    x = fashion_photos['x']
    y = fashion_photos['y']

    # 読み込んだデータを三次元配列に変換
    x = x.reshape(-1, im_rows, im_cols, im_color)
    x = x.astype('float32') / 255
    y = keras.utils.to_categorical(y.astype('int32'), num_classes)

    # 学習用とテスト用に分ける
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75)

    # CNNモデルを取得
    model = cnn_model_s.get_model(in_shape, num_classes)

    # モデルの学習
    hist = model.fit(x_train, y_train, batch_size=32, epochs=30, verbose=1, validation_data=(x_test, y_test))
    print(hist)

    #モデルを評価
    score = model.evaluate(x_test, y_test, verbose=1)
    print("正解率=", score[1], "loss=", score[0])
    # 学習したモデルを保存
    model.save_weights(str(num_classes)+'.hdf5')

    # 学習結果をグラフで表示
    #metrics = ['loss', 'accuracy']  # 使用する評価関数を指定
    #fig = plt.figure(figsize=(10, 5))  # グラフを表示するスペースを用意

    #for i in range(len(metrics)):

        #metric = metrics[i]

        #plt.subplot(1, 2, i+1)  # figureを1×2のスペースに分け、i+1番目のスペースを使う
        #plt.title(metric)  # グラフのタイトルを表示
    
        #plt_train = hist.history[metric]  # historyから訓練データの評価を取り出す
        #plt_test = hist.history['val_' + metric]  # historyからテストデータの評価を取り出す
    
        #plt.plot(plt_train, label='training')  # 訓練データの評価をグラフにプロット
        #plt.plot(plt_test, label='test')  # テストデータの評価をグラフにプロット
        #plt.legend()  # ラベルの表示
    
    #plt.show()  # グラフの表示
    #fig.savefig("test50_2.png")