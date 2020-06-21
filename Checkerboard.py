import cv2
import numpy as np

checker=np.zeros([480,480],dtype='uint8')

for i in range(60,480,120):
    for j in range(60,480,120):
        checker[i-60:i,j-60:j]=255
        checker[i:i+60,j:j+60]=255

cv2.imshow('8 * 8 Checkerboard',checker)
cv2.waitKey(0)
cv2.destroyAllWindows()
