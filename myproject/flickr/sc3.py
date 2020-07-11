import matplotlib.pyplot as plt
import numpy as np

# 사진 데이터 읽어들이기
photos = np.load('flickr/photos.npz')
x = photos['x']
y = photos['y']

# 시작 인덱스 --( 1)
idx = 0

#pyplot로 출력하기
plt.figure(figsize=(10, 10))

for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.title(y[i+idx])
    plt.imshow(x[i+idx])
plt.show()