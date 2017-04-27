import cv2
import numpy

frame=cv2.imread('image.jpg')


hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#color value for lower red level considering the noise,adjusted manually to find a particula r color in the image
lower_red = np.array([30,150,50])

#color value for higher red level considering the noise
higher_red= np.array([255,255,180])

kernel=np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

erosion=cv2.erode(mask, kernel,iterations = 1)
dilation=cv2.dilate(mask, kernel,iterations = 1)

cv2.imshow('Original', frame)
cv2.imshow('Mask',mask)
cv2.imshow('Erosion',mask)
cv2.imshow('Dilation',mask)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)

cv2.waitkey(5)

cv2.destroyAllWindows()
cap.release()
