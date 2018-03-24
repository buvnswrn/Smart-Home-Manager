import cv2, os
import numpy as np
from PIL import Image
recognizer1 = cv2.face.createLBPHFaceRecognizer(1,1,7,7)
recognizer2=cv2.face.createEigenFaceRecognizer(15)
path='dataset'
def img_id(path):

    # Get all file path
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    # Initialize empty face sample
    ImgList=[]
    
    # Initialize empty id
    ids = []

    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        img = Image.open(imagePath).convert('L')
        img=img.resize((110,110))
        # PIL image to numpy array
        img_np = np.array(img,'uint8')

        # Get the image id
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        ImgList.append(img_np)
        ids.append(Id)
        cv2.imshow("Data Training ",img_np)
        cv2.waitKey(1)
    print("Img List=",ImgList)
    return np.array(ids),ImgList
ids,ImgList=img_id(path)
print("Data is being Trained....." )
recognizer1.train(ImgList,ids)
recognizer2.train(ImgList,ids)
print('Data Training Complete')
recognizer1.save('trainer/trainedData1.xml')
recognizer2.save('trainer/trainedData2.xml')
print('Xml File saved.')
cv2.destroyAllWindows()
