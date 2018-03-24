from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import Id
camera = PiCamera()
camera.resolution=(160,128)
camera.framerate=32
rawCapture= PiRGBArray(camera, size=(160, 128))
face_detector = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade=cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
face_id = Id.AddName()
count = 0
WHITE=[255,255,255]
while (count < 200):
    ret,img = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if np.average(gray) > 110:
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            Face=gray[y-int(h/2):y+int(h*1.5),x-int(x/2):x+int(w*1.5)]
            eyes=(Id.DetectEyes(Face))
            cv2.putText(gray,"Face Detected",(x+(w/2),y-5),cv2.FONT_HERSHEY_DUPLEX,.4,WHITE)
            if eyes is not None:
                frame=eyes
            else:
                frame=gray[y:y+h,x:x+w]
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.waitKey(300)
            count += 1
    cv2.imshow('Capturing Face', img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
print('Completed')
camera.close()
cv2.destroyAllWindows()
