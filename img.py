import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:\\Users\\Swan Computers\\.vscode\\extensions\\word.jpg",1)


col=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# applying different thresholding 
# techniques on the input image
# all pixels value above 120 will 
# be set to 255
ret,thresh=cv2.threshold(col,120,255,cv2.THRESH_BINARY)
ret,thresh1=cv2.threshold(col,120,255,cv2.THRESH_BINARY_INV)
ret,thresh2=cv2.threshold(col,120,255,cv2.THRESH_TRUNC)
ret,thresh3=cv2.threshold(col,120,255,cv2.THRESH_TOZERO)
ret,thresh4=cv2.threshold(col,120,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Binary Threshold', thresh)
cv2.imshow('Binary Threshold Inverted', thresh1)
cv2.imshow('Truncated Threshold', thresh2)
cv2.imshow('Set to 0', thresh3)
cv2.imshow('Set to 0 Inverted', thresh4)
cv2.waitKey(0)
''' adptive threshold rather than applying  one threshold to whole image and compute 
the threshold of the small parts and applies 
two  adaptive method means and gussian 
syntax:cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)
cv2.ADAPTIVE_THRESH_MEAN_C: Threshold Value = (Mean of the neighbourhood area values – constant value). In other words, 
it is the mean of the blockSize×blockSize neighborhood of a point minus constant.

cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Threshold Value = (Gaussian-weighted sum of the neighbourhood values – constant value). In other words, 
it is a weighted sum of the blockSize×blockSize neighborhood of a point minus constant

-> blockSize: Size of a pixel neighborhood that is used to calculate a threshold value
'''
# no return value 
thresh5=cv2.adaptiveThreshold(col,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)
thresh6=cv2.adaptiveThreshold(col,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)

cv2.imshow('adaptive_mean', thresh5)
cv2.imshow('adaptive_gussian', thresh6)
cv2.waitKey(0)
'''
    Otsu Thresholding, a value of the threshold isn’t chosen
      but is determined automatically. the otus methdod apply bimodel means 
      the image having 2 peaks in the histogram
syntax:Syntax: cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)


'''
ret,thresh7=cv2.threshold(col,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otus_thresh', thresh7)
 


 
cv2.waitKey(0)
cv2.destroyAllWindows()
