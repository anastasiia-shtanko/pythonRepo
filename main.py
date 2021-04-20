import Child
import cv2 as cv
import imgProc


me = Child.Child("Anastasiia", 20, 158)
me.show()

myImg = imgProc.imgProc("shrek.jpg")
myImg2 = imgProc.imgProc("cosmos.jpg")

myImg.showImg()
myImg2.blurImg()
myImg.invertImg()

myImg.addTwoImg(myImg2.image)
myImg.substrTwoImg(myImg2.image)

cv.destroyAllWindows()
