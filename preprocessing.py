import cv2
import numpy as np
import math

GAUSSIAN_SMOOTH_FILTER_SIZE = (5, 5)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9

def preprocess(imgoriginal):

    height, width, numChannels = imgoriginal.shape

    HSVimg = np.zeros((height, width, 3), np.uint8)

    HSVimg = cv2.cvtColor(imgoriginal, cv2.COLOR_BGR2HSV)

    imgHue, imgSaturation, imgValue = cv2.split(HSVimg)

    height, width = imgValue.shape

    imgtop = np.zeros((height, width, 1), np.uint8)
    imgblack = np.zeros((height, width, 1), np.uint8)

    structuringelement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    imgtop = cv2.morphologyEx(imgValue, cv2.MORPH_TOPHAT, structuringelement)
    imgblack = cv2.morphologyEx(imgValue, cv2.MORPH_BLACKHAT, structuringelement)

    imgvalueplustophat = cv2.add(imgValue, imgtop)
    imgvalueplustophatminusblackhat = cv2.subtract(imgvalueplustophat, imgblack)

    imgblurred = np.zeros((height, width, 1), np.uint8)

    imgblurred = cv2.GaussianBlur(imgvalueplustophatminusblackhat, GAUSSIAN_SMOOTH_FILTER_SIZE, 0)

    imgthresh = cv2.adaptiveThreshold(imgblurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)

    return(imgthresh)
