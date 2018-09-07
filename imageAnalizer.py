import numpy as np
from skimage.measure import compare_ssim
import imutils
import cv2

def compareDifferenceInGrays(first,second):
	frameDelta = cv2.absdiff(first, second)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)

	# (score, diff) = compare_ssim(first, second, full=True)
	# diff = (diff * 255).astype("uint8")
	# print("SSIM: {}".format(score))
	# thresh = cv2.threshold(diff, 0, 255,
	# 	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	return thresh

def getThreshold(first,second):
	imageA = cv2.imread(first)
	imageB = cv2.imread(second)

	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	grayA = cv2.GaussianBlur(grayA, (21, 21), 0)
	grayB = cv2.GaussianBlur(grayB, (21, 21), 0)

	return compareDifferenceInGrays(grayA,grayB)

def erodeImageContorns(image):
	kernel = np.ones((10,10),np.uint8)
	return cv2.erode(image,kernel,iterations = 1)

def saveImageAs(name, newName):
	image = cv2.imread(name)
	cv2.imwrite(newName, image)

def whitePixelsPercentage(image_GRAY):
	white_pixel = cv2.countNonZero(image_GRAY)
	total_pixel = image_GRAY.shape[0] * image_GRAY.shape[1]
	return (white_pixel * 100 / float(total_pixel))

