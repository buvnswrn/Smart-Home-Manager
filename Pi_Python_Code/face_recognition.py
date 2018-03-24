from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import Id as findid
import db
def recognise():
    facecascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
    eye = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
    spec = cv2.CascadeClassifier('Haar/haarcascade_eye_tree_eyeglasses.xml')
    count=0
    recognizer1 = cv2.face.createLBPHFaceRecognizer()
    recognizer2=cv2.face.createEigenFaceRecognizer()
    recognizer1.load('trainer/trainedData1.xml')
    recognizer2.load('trainer/trainedData2.xml')
    username="Bhuvan"
    # Initialize and start the video frame capture
    cam = PiCamera()
    cam.resolution = (160, 120)
    cam.framerate = 32
    rawCapture = PiRGBArray(cam, size=(160, 120))

    # allow the camera to warmup
    time.sleep(0.1)
    lastTime = time.time()*1000.0


    # Loop
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # Read the video frame
        image = frame.array

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
        print time.time()*1000.0-lastTime," Found {0} faces!".format(len(faces))
        lastTime = time.time()*1000.0
        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            #cv2.rectangle(img, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
            cv2.circle(image, (x+w/2, y+h/2), int((w+h)/3), (255, 255, 255), 1)
            facecrp=cv2.resize((gray[y:y+h,x:x+w]),(110,110))
            # Recognize the face belongs to which ID
            Id,confidence = recognizer1.predict(facecrp)
            Id1,confidence1=recognizer2.predict(facecrp)
            
            # Check the ID if exist 
            Name=findid.ID2Name(Id,confidence)
            Name2=findid.ID2Name(Id1,confidence1/100)
            print("Eigen:",Name)
            print("LBPH",Name2)
#           print(Id1,confidence1,Name,Name2,username,count)
    
            if(count==0):
                username=Name2
                count+=1
            if(count>0 and username==Name2):
                count+=1
            if count==10:
                break
            findid.DispID(x,y,w,h,Name,gray)
            if Name2 is not None:
                cv2.putText(image, Name2, ((x+w/2-(len(Name2)*7/2)), y-20), cv2.FONT_HERSHEY_DUPLEX, .4, [255,255,255])
            else:
                findid.DispID(x,y,w,h,"Face Not Recognized",gray)
        
        cv2.imshow('Face',image)
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if count==10:
            break
    print(username)
    cv2.imwrite("tmp/face.jpg",image)
    db.fetch(username,"tmp/face.jpg")
    cam.close()
    cv2.destroyAllWindows()
    return username
# recognise()
