import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
The codes below are used to remove the outer artifacts
To run, 1.check the path directory 2.run python file
'''

path = '020118-05_pos000_1_6.jpg'
ori_img = cv.imread(path)
gray_img = cv.cvtColor(ori_img, cv.COLOR_BGR2GRAY)

thresh, blackAndWhiteImage = cv.threshold(gray_img, 240, 255, cv.THRESH_BINARY)
cnt= cv.findContours(blackAndWhiteImage,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]

# Find the contour that has area less than 800
contour = []
for i in range(1, len(cnt)):
    this_area = cv.contourArea(cnt[i])
    if this_area < 800:
        contour.append(cnt[i])


def draw_mask(cnts):
    mask = np.zeros(gray_img.shape[:2], dtype="uint8")
    cv.drawContours(mask, cnts, -1, 255, thickness=cv.FILLED)
    return mask

mask = draw_mask(contour)
# cv.imshow("Mask", mask)

out = cv.inpaint(ori_img,mask,3,cv.INPAINT_TELEA)

# cv.drawContours(ori_img, contour, -1, (0, 0, 0), 3)
# cv.imshow('img',ori_img)
cv.imshow('img',out)
cv.waitKey(0)


