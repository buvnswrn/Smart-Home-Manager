import os
import imagebot as imgbot
from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
#    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("tmp/guest.jpg",img)
cam.release()
imgbot.sendimage("tmp/guest.jpg")
os.remove("tmp/guest.jpg")
