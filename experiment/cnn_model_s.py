# CNNモデルの定義
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam


# CNNモデルを定義して返却する関数
def get_model(in_shape, num_classes):

  # 特徴量抽出

  # Seqentialモデルのインスタンスを作成
  model = Sequential()
  # 層を積み重ねる
  model.add(Conv2D(16,3,input_shape=in_shape))  # 畳み込みフィルタ層
  model.add(Activation('relu'))                 # 最適化関数
  model.add(Conv2D(32,3))
  model.add(Activation('relu'))
  model.add(MaxPool2D(pool_size=(2,2)))         # プーリング層
  model.add(Conv2D(64,3))
  model.add(Activation('relu'))
  model.add(MaxPool2D(pool_size=(2,2)))

  # 特徴量に基づいた分類
  model.add(Flatten())                          # 全結合層入力のためのデータの一次元化
  model.add(Dense(1024))                        # 全結合層
  model.add(Activation('relu'))                 # 最適化関数
  model.add(Dropout(0.5))                       # ドロップアウト層
  model.add(Dense(num_classes, activation='softmax'))  # 出力層

  # モデルのコンパイル
  adam = Adam(lr=1e-4)
  model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=["accuracy"])
  
  return model