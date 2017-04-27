import cv2
import numpy as np

img=cv2.imread('image.jpg')
grayscaled=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold=cv2.adaptiveThreshold(grayscaled,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1)
retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Otsu threshold',threshold2)
cv2.imshow('original', img)
cv2.imshow('adaptve threshold', threshold)
cv2.imshow('gray scale', grayscaled)
cv2.waitKey(0)
cv2.detroyAllWindows()
