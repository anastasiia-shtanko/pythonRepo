import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class imgProc:
    def __init__(self, image):
        self.image = image

    def showImg(self):
        img = cv.imread(self.image)
        cv.imshow("Image", img)
        cv.waitKey(0)

    def addTwoImg(self, image2):
        img = cv.imread(self.image)
        img2 = cv.imread(image2)
        weightedSum = cv.addWeighted(img, 0.5, img2, 0.4, 0)
        cv.imshow('Weighted Image', weightedSum)
        cv.waitKey(0)

    def substrTwoImg(self, image2):
        img = cv.imread(self.image)
        img2 = cv.imread(image2)
        sub = cv.subtract(img, img2)
        cv.imshow('Subtracted Image', sub)
        cv.waitKey(0)

    def blurImg(self):
        img = cv.imread(self.image)
        blur = cv.blur(img, (100, 100))
        plt.subplot(121), plt.imshow(img), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def invertImg(self):
        img = cv.imread(self.image)
        dest_not = cv.bitwise_not(img, mask=None)
        cv.imshow('Inverted image', dest_not)
        cv.waitKey(0)