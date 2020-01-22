from preprocessing import preprocess 
import cv2

image_file = "images/1.png"
imgoriginal = cv2.imread(image_file)
imgex = preprocess(imgoriginal)

cv2.imshow("image", imgex)
cv2.waitKey(0)
