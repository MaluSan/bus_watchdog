import time
import imageAnalizer
import camera
import cv2

def timestamp():
	t = time.localtime()
	stamp = '%d-%02d-%02d-%02d%02d%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
	return stamp +'.jpg'

files_route = '/home/malu/Documents/bus/'
basePhotoDir = files_route + 'empty.jpg'
prevPhotoDir = files_route + 'prev.jpg'
newPhotoDir  = files_route + 'new.jpg'
logPhotoDir  = files_route + '/log/'
bufferPhotoDir  = files_route + '/fotos/'

timeOfPhoto = timestamp()
print(timeOfPhoto)

camera.takePhoto(newPhotoDir)
prev_thresh = imageAnalizer.getThreshold(basePhotoDir,prevPhotoDir)
new_thresh  = imageAnalizer.getThreshold(basePhotoDir,newPhotoDir)
thresh = imageAnalizer.compareDifferenceInGrays(prev_thresh,new_thresh)

erosion = imageAnalizer.erodeImageContorns(thresh)
ratio = imageAnalizer.whitePixelsPercentage(erosion)
print(ratio)

if ratio > 5:
	imageAnalizer.saveImageAs('new.jpg',logPhotoDir+timeOfPhoto)
	imageAnalizer.saveImageAs('new.jpg','prev.jpg')

imageAnalizer.saveImageAs(newPhotoDir,bufferPhotoDir+timeOfPhoto)

cv2.imshow('1',thresh)
cv2.imshow('2',erosion)
cv2.waitKey(0)