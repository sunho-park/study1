# keras112_cifar 복사
# regularizer 정규화

'''
가중치값 자체가 백만으로 커지면 relu 3번 만나면 가중치값 떡상함... w1x1+w2x2+w3x3 
L1 규제 : 가중치의 절대값 합
regularizer.l1(l=0.01)
L2 규제 : 가중치의 제곱 합
regularizer.l2(l=0.01)

loss = L1*reduce_sum(abs(x)) 
loss = L2*reduce_sum(square(x))

그 다음 레이어로 전달되는 가중치 값을 줄이겠다.



'''

from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential, Model, Input

from keras.layers import Dense, LSTM, Conv2D
from keras.layers import Flatten, MaxPooling2D, Dropout
from keras.optimizers import Adam

import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = cifar10.load_data()


# 데이터 전처리 1. 원핫인코딩

# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)

# 정규화 / 피처를 늘린다 / 레귤러라리 제이션

# 데이터 전처리 2. 정규화
x_train = x_train.reshape(50000, 32, 32, 3).astype('float32')/255
x_test = x_test.reshape(10000, 32, 32, 3).astype('float32')/255

# 모델 구성 
from keras.regularizers import l1, l2, l1_l2

model = Sequential()
model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))

model.add(Conv2D(64, kernel_size=3, padding='same', activation='relu', kernel_regularizer=l2(0.001)))
model.add(Conv2D(64, kernel_size=3, padding='same', activation='relu', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))

model.add(Conv2D(128, kernel_size=3, padding='same', activation='relu', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, kernel_size=3, padding='same', activation='relu', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))

model.add(Flatten())
model.add(Dense(256, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dense(10, activation='softmax'))

model.summary()

# 훈련
model.compile(optimizer=Adam(1e-4), loss='sparse_categorical_crossentropy', metrics=['acc']) 
# 따옴표'adam' 디폴트의 adam을 가져옴 / 1e-4 0.0001 / 원한인코딩안했을 경우 sparse_categorical_crossentropy 

hist = model.fit(x_train, y_train, epochs=20, batch_size=32, verbose=1, validation_split=0.3)

# 평가, 예측
loss_acc = model.evaluate(x_test, y_test, batch_size=32)

loss = hist.history['loss']
val_loss = hist.history['val_loss']
acc = hist.history['acc']
val_acc = hist.history['val_acc']

print("loss_acc : ", loss_acc)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)

plt.plot(hist.history['loss'], marker='.', c='red', label='loss')
plt.plot(hist.history['val_loss'], marker='.', c='blue', label='val_loss')

plt.grid()
plt.title('loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(loc='upper right')

plt.subplot(2, 1, 2)

plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])

plt.grid()
plt.title('acc')
plt.ylabel('acc')
plt.xlabel('epoch')
plt.legend(['acc', 'val_acc'])

plt.show()


