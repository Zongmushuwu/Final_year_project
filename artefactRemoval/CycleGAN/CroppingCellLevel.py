import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

'''
The codes below are used for data pre processing for CycleGAN model. To run, check the rootpath and run Python file.
The codes crop each image into 160*160 and with only one complete cell in each image
'''

rootpath = 'artefactRemoval/'

# Create new data folder for seperate img
new_goodpath = rootpath + 'cropped/good'
new_badpath = rootpath + 'cropped/bad'
if not os.path.exists(new_goodpath):
    os.makedirs(new_goodpath)
if not os.path.exists(new_badpath):
    os.makedirs(new_badpath)

old_goodpath = rootpath + 'sepData/good'
old_badpath = rootpath + 'sepData/bad'

# Crop each image into 160*160 and with only one complete cell in each image
def cropping(ori_path, writeroot):
    for file in os.listdir(ori_path):
        if not file.startswith('.'):
            # print(file)
            path = os.path.join(ori_path, file)
            path_list = ori_path.split('/')
            writepath_r = writeroot +'/'+ file

            ori_img = cv.imread(path)
            shape = ori_img.shape
            width = shape[0]
            height = shape[1]

            gray_img = cv.cvtColor(ori_img, cv.COLOR_BGR2GRAY)
            mean = cv.mean(gray_img)
            thr = mean[0]

            thresh, blackAndWhiteImage = cv.threshold(gray_img, thr/1.3, 255, cv.THRESH_TOZERO)
            cnt, hierarchy = cv.findContours(blackAndWhiteImage,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

            # find the box containing only one complete cell
            contours = []
            box = []
            for k in range(len(cnt)):
                if 300 < cv.arcLength(cnt[k],True) < 2500:
                    contours.append(cnt[k])
                    x,y,w,h = cv.boundingRect(cnt[k])
                    box.append([x,y,w,h])

            # draw squared cropping box in size 160*160
            croppingbox = []
            for k in range(len(box)):
                x,y,w,h = box[k]
                if w <= 160 or h <= 160:
                    addingw = 160 - w
                    addingh = 160 - h
                    addx = int(addingw / 2)
                    addy = int(addingh / 2)
                    x = x - addx
                    y = y - addy
                    w = 160
                    h = 160
                    if x > 0 and y > 0 and x+w < width and y+h < height:
                        croppingbox.append([x,y,w,h])
            
            # write the cropped image
            for k in range(len(croppingbox)):
                x,y,w,h = croppingbox[k]
                crop = ori_img[y:y+h,x:x+w]
                writepath_l = writepath_r.split('.')
                writepath = writepath_l[0]+ '_' + str(k) + '.' + writepath_l[1]
                cv.imwrite(writepath,crop)


cropping(old_goodpath,new_goodpath)
cropping(old_badpath,new_badpath)