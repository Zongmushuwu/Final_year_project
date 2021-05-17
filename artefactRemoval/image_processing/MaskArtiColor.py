import cv2 as cv
import numpy as np
import os

'''
To run, 1.check the root and path 2.run the python file
'''
# Masking different colors
root = 'artefactRemoval/rawData/bad'
path = '020118-05/pos001_EDOF_DENISOVAN_RGB.tiff'
file_path = os.path.join(root,path)

img = cv.imread(file_path)
low = np.array([0,0,0])
high = np.array([100,100,100])
mask = cv.inRange(img, low, high)
cv.imshow('Result',mask)
cv.waitKey(0)

