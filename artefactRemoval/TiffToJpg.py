import cv2
import os

'''
The codes below are used for data pre processing. To run, check the rootpath and run Python file.
To change .tiff to .jpg and to change data directory from:
    ----bad
        ----020118-05
            ----pos000_EDOF_DENISOVAN_RGB.tiff
            ----pos001_EDOF_DENISOVAN_RGB.tiff
            ...
        ----050418-02
        ...
    ----good
        ...
to:
    ----bad
        ----020118-05_pos000.jpg
        ----020118-05_pos001.jpg
        ...
    ----good
        ...
'''
rootpath = 'artefactRemoval/'

# Create new data folder for seperate img
new_goodpath = rootpath + 'sepData/good'
new_badpath = rootpath + 'sepData/bad'
if not os.path.exists(new_goodpath):
    os.makedirs(new_goodpath)
if not os.path.exists(new_badpath):
    os.makedirs(new_badpath)

# Seperate img into only two folders -- good and bad AND from .tiff to .jpg
raw_rootdir = rootpath + 'rawData/'
raw_gooddir = raw_rootdir + 'good'
raw_baddir = raw_rootdir + 'bad'

def seperator(dir, quality):
    writeroot = rootpath + 'sepData/' + quality
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if not file.startswith('.'):
                path = os.path.join(subdir, file)
                path_list = path.split('/')
                writepath = writeroot +'/'+ path_list[-2] + '_'+ path_list[-1].split('_EDOF')[0]+'.jpg'
                # print(writepath)
                img = cv2.imread(path)
                # from .tiff to .jpg
                cv2.imwrite(writepath,img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])

seperator(raw_gooddir,'good')
seperator(raw_baddir,'bad')