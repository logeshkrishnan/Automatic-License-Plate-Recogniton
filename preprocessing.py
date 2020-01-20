import cv2
import numpy as np
import math

image_file = "images/1.png"

input_image = cv2.imread(image_file)

height, width, numChannels = input_image.shape

HSVimg = np.zeros((height, width, 3), np.uint8)

HSVimg = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

imgHue, imgSaturation, imgValue = cv2.split(HSVimg)

print(imgValue)

#grayscaleimg = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#cv2.imshow(HSVimg, "sample")
