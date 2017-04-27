import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)

#cv2.imshow('imagefield',img)
#cv2.waitkey(0)
#cv2.destroyAllWindows()
plt.imshow(img, cmap = 'gray' , interpolation= 'bicubic')
plt.xticks([]), plt.yticks([])
plt.plot([200,300,400],[100,200,300],'c',linewidth=5)
plt.show()
