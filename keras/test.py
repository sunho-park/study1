from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

# 1. 데이터

x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])

y = array([4, 5, 6, 7])        

print("x.shape : ", x.shape)   #(4, 3)
print("y.shape : ", y.shape)   #(4, ) 스칼라4개짜리

print(x)
# x = x.reshape(4, 3, 1)       #검산 전부곱해봐서 같으면 됨(4, 3), (4, 3, 1)
x = x.reshape(x.shape[0], x.shape[1], 1)

print(x)
print(x.shape)

# 모델구성
model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(3, 1)))
model.add(Dense(20))
model.add(Dense(20))
model.add(Dense(1))
model.summary()

# 3. 실행
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=500, batch_size=1)

x_input = array([5, 6, 7])  # 스칼라

print("x_input", x_input)
print("x_input.shape", x_input.shape)
x_input = x_input.reshape(1, 3, 1)

print("x_input : ",x_input)
print("x_input : ", x_input)

yhat = model.predict(x_input)
print(yhat)






