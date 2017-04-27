import numpy as np
import cv2

img=cv2.imread('image.jpg',cv2.IMREAD_COLOR)

pts=np.array([[10,5],[20,30],[70,20],[50,10]] , np.int32)

cv2.polylines(img, [pts] ,True, (0,255,255) ,3)

font =cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,'OpenCV Tuts!',(10,50), font, 1, (200,255,155), 2, cv2.CV_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
