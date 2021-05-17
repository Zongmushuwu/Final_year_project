import cv2 as cv
import numpy as np

'''
The codes below are used to remove the inner artifacts
To run, 1.check the path directory 2.run python file
'''

path = 'Outer_removed.png'
ori_img = cv.imread(path)
gray_img = cv.cvtColor(ori_img, cv.COLOR_BGR2GRAY)
mean = cv.mean(gray_img)
thr = mean[0]

# To get small, noises(very small) and large areas
def get_area(contours):
    small_area = []
    very_small_area = []
    large_area = []
    for i in range(0,len(contours)):
        this_area = cv.contourArea(contours[i])
        if this_area < 50:
            small_area.append(this_area)
        if this_area < 2:
            very_small_area.append(this_area)
        if this_area > 50:
            large_area.append(this_area)
    return small_area, very_small_area, large_area

# To calculate number of small, large areas and noise
# and get the corresponded contours
num_small_area = []
num_very_small_area = []
num_large_area = []
contour = []
for k in np.arange(1.5 ,3.0 ,0.1):
    thresh, blackAndWhiteImage = cv.threshold(gray_img, thr/k, 255, cv.THRESH_BINARY)
    cnt= cv.findContours(blackAndWhiteImage,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    small_area, very_small_area, large_area = get_area(cnt)
    num_small_area.append(len(small_area))
    num_very_small_area.append(len(very_small_area))
    num_large_area.append(len(large_area))
    contour.append(cnt)

# To get the top 5 number of small areas
idx_top_5_small = np.argpartition(num_small_area,-5)[-5:]
idx_top_5_small = np.flipud(idx_top_5_small)
selected_num_large_area = [num_large_area[idx_top_5_small[0]],num_large_area[idx_top_5_small[1]],num_large_area[idx_top_5_small[2]],num_large_area[idx_top_5_small[3]],num_large_area[idx_top_5_small[4]]]

# From the 5 selected number of area, find the bottom 2 number of large areas
idx_bottom_2_large = np.argsort(selected_num_large_area)[:2]
idx_very_small = idx_top_5_small[idx_bottom_2_large]
idx_very_small = np.flipud(idx_very_small)
selected_num_very_small_area = [num_very_small_area[idx_very_small[0]],num_very_small_area[idx_very_small[1]]]

# From the 2 selected number of area, find the one with min number of noises
idx_bottom_1_very_small = np.argmin(selected_num_very_small_area)

# find the idx of the selected number of area
idx = idx_very_small[idx_bottom_1_very_small]
print(idx)

# get the contour corresponded to the idx of the selected number of area
qualified = contour[idx]
           
# except the outer one
qualified = qualified[1:]

def draw_mask(cnts):
    mask = np.zeros(gray_img.shape[:2], dtype="uint8")
    cv.drawContours(mask, cnts, -1, 255, thickness=cv.FILLED)
    return mask
mask = draw_mask(qualified)

# image inpainting
out = cv.inpaint(ori_img,mask,3,cv.INPAINT_TELEA)

# To draw images with the contours found
# cv.drawContours(ori_img, qualified, -1, (0, 0, 0), 3)
# cv.imshow('img',ori_img)

# To draw the masks
# cv.imshow("Mask", mask)

# To remove show the inner artifacts removed image
cv.imshow('img',out)
cv.waitKey(0)

