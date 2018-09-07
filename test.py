from skimage.measure import compare_ssim
import imutils
import cv2
import numpy as np

files_route = '/home/malu/Documents/bus/'
image = cv2.imread(files_route + 'new.jpg')
cv2.imwrite(files_route + 'aux.jpg', image)

# cv2.imshow("1", grayA)
# cv2.imshow("2", erosion1)

# cv2.waitKey(0)

