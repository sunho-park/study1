'''from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM


x=np.array(range(1, 101))
y=np.array([range(101, 201), range(711, 811), range(100)])

y = np.transpose(y)'''
from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

a= array([[1,2,3], [1,2,3]])
b= array([[[1,2], [4,3]], [[4,5], [5,6]]])
c= array([[[1],[2],[3]], [[4],[5],[6]]])
d= array([[[1,2,3,4]]])
e= array([[[[1],[2]]], [[[3],[4]]]])

print("a : ", a.shape)
print("b : ", b.shape)
print("c : ", c.shape)
print("d : ", d.shape)
print("e : ", e.shape)


