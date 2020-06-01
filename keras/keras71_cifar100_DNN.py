from keras.datasets import cifar100
from keras.utils import np_utils
from keras.models import Sequential, Model, Input

from keras.layers import Dense, LSTM, Conv2D
from keras.layers import Flatten, MaxPooling2D, Dropout

import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = cifar100.load_data()

print('x_train[0] : ', x_train[0])
print('y_train[0] : \n', y_train[0])
'''if 99 in y_train:
    print('yes')
else:
    print('no')'''
print("y_train : \n", y_train)
print("y_test : ", y_test)
print("y_train.shape : ", y_train.shape)
print("y_test.shape : ", y_test.shape)


# plt.imshow(x_train[0])
# plt.show()

# 데이터 전처리 1. 원핫인코딩

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)


# 데이터 전처리 2. 정규화
x_train = x_train.reshape(50000, 32*32*3).astype('float32')/255
x_test = x_test.reshape(10000, 32*32*3).astype('float32')/255

# 모델 구성 함수형
input1 = Input(shape=(32*32*3, ))

dense1_1 = Dense(256, activation='relu')(input1)

dense1_2 = Dense(512, activation='relu')(dense1_1)
dense1_2 = Dropout(0.1)(dense1_1)

# dense1_3 = Dense(512, activation='relu')(dense1_2)
# dense1_3 = Dropout(0.2)(dense1_2)

output1 = Dense(1024, activation='relu')(dense1_2)
output1 = Dropout(0.3)(dense1_2)

# output2_2 = Dense(1024, activation='relu')(output1)
# output2_2 = Dropout(0.4)(output1)

output3_3 = Dense(1024, activation='relu')(output1)
output3_3 = Dropout(0.5)(output1)

output4_4 = Dense(100, activation='softmax')(output3_3)
model = Model(inputs= input1, outputs= output4_4)

# 컴파일, 훈련
from keras.callbacks import EarlyStopping, ModelCheckpoint

early_stopping = EarlyStopping(monitor='loss', patience=20)

modelpath = './model/sample/cifar100/check={epoch:02d}-{val_loss:.4f}.hdf5'

checkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss', save_best_only=True, mode='auto')

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
hist = model.fit(x_train, y_train, epochs=15, batch_size=64, verbose=1, validation_split=0.4, callbacks=[early_stopping, checkpoint])

model.save('./model/sample/cifar100/cifar100_model_save.h5')    
model.save_weights('./model/sample/cifar100/cifar100_weights.h5')    

# 평가, 예측

loss_acc = model.evaluate(x_test, y_test)

loss = hist.history['loss']
val_loss = hist.history['val_loss']
acc = hist.history['acc']
val_acc = hist.history['val_acc']

print("acc : ", acc)
print("val_acc : ", val_acc)
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

model.save('./model/sample/cifar100/71_cifar100_dnn.py')