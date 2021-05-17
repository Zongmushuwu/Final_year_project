import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

''' 
Referencing codes in official OpenCV website about image thresholding.
OpenCV; Title:  Image Thresholding
URL: https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html
'''

'''
The codes below are used to test each image binarization techniques, 
To run, 1.check the path directory 2.run python file
'''

path = '020118-05_pos000_0_1.jpg'

ori_img = cv.imread(path)
gray_img = cv.cvtColor(ori_img, cv.COLOR_BGR2GRAY)

ret,th1 = cv.threshold(gray_img,100,255,cv.THRESH_BINARY)
ret2,th2 = cv.threshold(gray_img,240,255,cv.THRESH_BINARY)
ret3,th3 = cv.threshold(gray_img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
th4 = cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,99,2)
th5 = cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,8)


titles = ['Grey Image', 'THRESH_BINARY Thresholding (thr = 100)',
            'THRESH_BINARY Thresholding (thr = 240)','Otsu\'s Thresholding', 
            'Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
images = [gray_img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()