import Child
import cv2 as cv
import imgProc


me = Child.Child("Anastasiia", 20, 158)
me.show()

myImg = imgProc.imgProc("shrek.jpg")
myImg2 = imgProc.imgProc("cosmos.jpg")

myImg.showImg("Beware ogre")
myImg2.blur()
myImg.invert()
myImg2.resize()
myImg.erode()

myImg.addTwoImgs(myImg2.image)
myImg.substrTwoImgs(myImg2.image)

myImg.crown()

cv.destroyAllWindows()
