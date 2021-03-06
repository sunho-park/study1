import cv2
import numpy as np

print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread(r'C:\Users\bitcamp\Desktop\opencv_dnn_202005\nomadProgramerIcon.png')
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2]
center = (width // 2, height // 2)
 
cv2.imshow("nomadProgramer", img)

mask = np.zeros(img.shape[:2], dtype = "uint8")
print(mask)
print(mask.shape)   # (653, 653)
cv2.circle(mask, center, 300, (255, 255, 255), -1)

cv2.imshow("mask", mask)
 
masked = cv2.bitwise_or(img, img, mask = mask) # bitwise AND, OR, NOT, and XOR operations
cv2.imshow("nomadProgramer with mask", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()