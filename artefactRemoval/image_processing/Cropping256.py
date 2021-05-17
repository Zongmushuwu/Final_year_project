import cv2
import os

'''
The codes below are used to crop each image into 256*256 for image processing.
To run, just run the Python file.
'''

# Create new data folder for seperate img
root = 'artefactRemoval/'
rootpath = root + 'cropped256/'
new_goodpath = rootpath + 'good'
new_badpath = rootpath + 'bad'
if not os.path.exists(new_goodpath):
    os.makedirs(new_goodpath)
if not os.path.exists(new_badpath):
    os.makedirs(new_badpath)

# Cropping img into 256*256
rootdir = root + 'sepData'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path = os.path.join(subdir, file)
        # print(path)
        path_list = path.split('/')
        label = path_list[-2]
        dirname = path_list[-1].split('.')[0]
        im = cv2.imread(path)
        for r in range(8):
            for c in range(10):
                writepath = rootpath + f'{label}/{dirname}_{r}_{c}.jpg'
                cv2.imwrite(writepath,im[r*256:(r+1)*256, c*256:(c+1)*256]) # r->row c->column