import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

# 1. 데이터
x= np.array(range(1,11))
print(x)
y = 5

def split_x(seq, y):
    aaa= []

    for i in range(len(seq) - y + 1):    #range(6)    #0, 1, 2, 3, 4, 5
        print("i : ", i)
        subset = seq[i : (i+y)]
        print("subset : ", subset)
        aaa.append([item for item in subset])
        
   # print(type(aaa)) list
    return np.array(aaa)

dataset =split_x(x, y)
print(dataset)

print("========================================================")


