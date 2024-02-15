import numpy as np
import cv2

originalImage= cv2.imread('class65/lion.png')
#print(originalImage)
print(originalImage.shape)

resizedImage= cv2.resize(originalImage,(500,500))


#grayscaleImage
grayScaleImage= cv2.cvtColor(resizedImage,cv2.COLOR_BGR2GRAY)

# oil paint
#oilPainting=cv2.xphoto.oilPainting(resizedImage, size=7,dynRation = 1)

invertedImage=255-grayScaleImage
blurredImg = cv2.GaussianBlur(invertedImage,(21,21),0)
sketchImage=cv2.divide(grayScaleImage, 255-blurredImg, scale=256)


cv2.imshow("Lion",resizedImage)
#cv2.imshow("Oil",oilPainting)
cv2.imshow("Gray",grayScaleImage)
cv2.imshow("blur",blurredImg)
cv2.imshow("sketch",sketchImage)
cv2.imshow("invert",invertedImage)
cv2.waitKey(0)

