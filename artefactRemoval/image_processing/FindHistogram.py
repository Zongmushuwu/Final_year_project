import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

''' 
Referencing codes in official OpenCV website about finding histogram.
OpenCV; Title: Histograms - 1 : Find, Plot, Analyze !!! 
URL: https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html
'''

'''
The codes below are used to find the image histogram of all images, 
zoomed-in of the first image and a perticular image.

To find image histogram of all images or the zoom-in one for the first image, 
1.check the root directory
2.uncomment either find_all() or find_zoomin_first()

To find image histogram of one image,
1.check the directory in variable img
2.uncomment find_one_hist()
'''

# Find all histograms
root = 'artefactRemoval/rawData/bad'
arti_0_path = ['020118-05']
arti_1_path = ['310718-15']
arti_2_path = ['050418-02']
arti_3_path = ['170718-43']
arti_4_path = ['090718-19','090818-18','230718-04r1']

all_path = [arti_0_path, arti_1_path, arti_2_path, arti_3_path, arti_4_path]

# find the histogram of one image
def find_histogram(img):
    color = ['b', 'g', 'r']
    histr = []
    for w,col in enumerate(color):
        hist = cv.calcHist([img], [w], None, [256], [0,256])
        hi = np.squeeze(hist)
        histr.append(hi)
    return histr

all_histr = []
for i, arti_path in enumerate(all_path):
    a_kind_histr = []
    for k, rt_path in enumerate(arti_path):
        path = os.path.join(root,rt_path)
        for file in os.listdir(path):
            if not file.startswith('.'):
                p = os.path.join(path, file)
                img = cv.imread(p)
                hist = find_histogram(img)
                a_kind_histr.append(hist)
    all_histr.append(a_kind_histr)

# To find the mean histogram for all images
def find_all():
    for i, a_kind_histr in enumerate(all_histr):
        mean = np.mean(a_kind_histr,axis=0)
        max = np.max(a_kind_histr,axis=0)
        min = np.min(a_kind_histr,axis=0)
        # std = np.std(a_kind_histr,axis=0)
        color = ['b', 'g', 'r']
        fig, ax = plt.subplots()
        x = np.arange(0,256,1)
        for i,col in enumerate(color):
            ax.plot(x,mean[i],color = col)
            # s = mean[i]-std[i]
            ax.fill_between(x,min[i],max[i],alpha=0.2,color = col)

# To zoom in the first artifact
def find_zoomin_first():
    for i, a_kind_histr in enumerate(all_histr):
        mean = np.mean(a_kind_histr,axis=0)
        std = np.std(a_kind_histr,axis=0)
        color = ['b', 'g', 'r']
        fig, ax = plt.subplots()
        x = np.arange(0,255,1)
        for i,col in enumerate(color):
            meani = mean[i][:-1]
            stdi = std[i][:-1]
            ax.plot(x,meani,color = col)
            s = meani-stdi
            ax.fill_between(x,meani-stdi,meani+stdi,alpha=0.2,color = col)

# Find a histogram of one image
def find_one_hist():
    img = cv.imread('artefactRemoval/rawData/bad/020118-05/pos001_EDOF_DENISOVAN_RGB.tiff')
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])


find_all()
# find_zoomin_first()
# find_one_hist()

plt.show()


