import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class imgProc:
    def __init__(self, path):
        self.image = cv.imread(path)

    def showImg(self, headerstr, flag=True, image=0):
        if flag == True:
            image = self.image
        cv.imshow(headerstr, image)
        cv.waitKey(0)

    def addTwoImgs(self, image2):
        weightedSum = cv.addWeighted(self.image, 0.5, image2, 0.4, 0)
        weightedSum = cv.putText(weightedSum, "Cosmic Shrek", (110, 295), cv.FONT_HERSHEY_SIMPLEX,
                                 2, (255, 0, 255), 3)
        self.showImg("Weighted image", False, weightedSum)

    def substrTwoImgs(self, image2):
        sub = cv.subtract(self.image, image2)
        self.showImg('Subtracted Image', False, sub)

    def blur(self):
        blur = cv.blur(self.image, (100, 100))
        plt.subplot(121), plt.imshow(self.image), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def invert(self):
        dest_not = cv.bitwise_not(self.image, mask=None)
        self.showImg('Inverted image', False, dest_not)

    def resize(self):
        y = int(input("Enter desired height:"))
        x = int(input("Enter desired width:"))
        rszd = cv.resize(self.image, (x, y))
        self.showImg("Resized image", False, rszd)

    def erode(self):
        kernel = np.ones((5, 5), np.uint8)
        img = cv.erode(self.image, kernel)
        self.showImg("Eroded image", False, img)

    def crown(self):
        color = (32, 165, 218)
        thickness = 7
        crownimage = cv.line(self.image, (310, 55), (374, 59), color, thickness)
        crownimage = cv.line(crownimage, (310, 55), (311, 15), color, thickness)
        crownimage = cv.line(crownimage, (374, 59), (382, 19), color, thickness)
        crownimage = cv.line(crownimage, (382, 19), (362, 36), color, thickness)
        crownimage = cv.line(crownimage, (311, 15), (330, 35), color, thickness)
        crownimage = cv.line(crownimage, (330, 35), (348, 14), color, thickness)
        crownimage = cv.line(crownimage, (362, 36), (348, 14), color, thickness)

        crownimage = cv.putText(crownimage, "Heh", (65, 65), cv.FONT_HERSHEY_SIMPLEX,
                                 1, (0, 0, 0), 3)

        self.showImg("Shrek in the crown", False, crownimage)
