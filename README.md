# Smart Home Manager
## Abstract
Smart Home Manager can be described as **Home Automation System (HAS) using Facial Recognition** that identifies users and enhances their in-home experience by automating the home according to their requirements. The system basically collects the user information and builds a profile for the user to automate the home appliances by identifying the user by using his *facial characteristics as input.*

The system collects the information about the required item used by the family members in their home through a web interface and stores the data. The system creates a profile and also captures the face of the family member. The system then uses the facial characters as an input, identifies the family member and distinguishes them from intruders and guest by interacting with the family member. The family members and neighbors are intimated about the intruder, if detected. The security is ensured every time, where user authentication is provided by two ways. *The captured face* as input in case of a registered user and *the family member’s response for the alert message* in case of guest. The family members are free to change their requirement through the web interface. The family members are distinguished from each other through their facial characteristics and thus the system is flexible between registered user and a guest user. The web interface is designed in HTML, CSS, JavaScript. The data is stored in MongoDB using PHP-Mongo Driver. The facial recognition and all image processing works are carried out using OpenCV-Python library. The Bot is designed to interact with family members using Slack API. The Notification part is achieved using Pushbullet API.

## Modules
**1.Profile Creation:**
   - Web interface creation
   - Collecting Data
   - Storing Data

**2.Dataset Collection**
   - Collect Name
   - Capture Faces

**3.Dataset Training**
   - Train using the Eigen classifier
   - Train using the LBPH classifier
   - Store as XML File
   
**4.Facial Recognition**
   - Motion sensor integration
   - Recognise Faces
   - Write names of recognised faces
   - Recognise unknown faces

**5.Switching Appliances ON:**
   - Fetch requirements of the user
   - Switch ON appliances connected to the ports
   - Switch OFF appliances connected to the ports
 
**6. Intruder Detection :**
   - Infrared sensor integration
   - Notify user
   - Bot message (Send and Receive message)
## Specifications Used
### Hardwares
   - Raspberry Pi 3 Model B 
   - Raspberry Pi Camera Module 
   - Motion Sensor
   - Infrared Sensor
   - 5V Relay (4 Channel)
   - Wires , bulb sockets, bulbs, GPIO Pins,Breadboard
### Softwares
   VNC Viewer <br/>
   XAMPP 
### Technologies
   **Programming Language:** Python, PHP <br/>
   **Web Server:**    Apache <br/>
   **Libraries:**   OpenCV, Numpy, PIL <br/> 
   **Data Storage:**   MongoDB <br/>
   **API:**    Pushbullet, Slack <br/>

## User interfaces
Login Screen:
![image](https://user-images.githubusercontent.com/20739181/37861000-ca6e23e8-2f56-11e8-9fa9-9d07107f46e0.png)
Sign Up Screen:
![image](https://user-images.githubusercontent.com/20739181/37861151-9cfa3bf6-2f59-11e8-888a-420a481d8e81.png)
Requirements Screen:
![image](https://user-images.githubusercontent.com/20739181/37861152-9f6f3846-2f59-11e8-8bfa-50528f33da66.png)
Requirements Screen (Edit Option):
![image](https://user-images.githubusercontent.com/20739181/37861154-b10faf72-2f59-11e8-9ca8-869ed840f79a.png)
Adding Person:
![image](https://user-images.githubusercontent.com/20739181/37861175-1f5b5620-2f5a-11e8-8085-8b3c6f23748f.png)
Modifying A Person:
![image](https://user-images.githubusercontent.com/20739181/37861176-219eb18e-2f5a-11e8-92c0-edf7927037b4.png)
Slack Bot (User Responding "Yes"):
![image](https://user-images.githubusercontent.com/20739181/37861177-26cf607c-2f5a-11e8-9556-210fd989bc4b.png)
Slack Bot (User Responding "No"):
![image](https://user-images.githubusercontent.com/20739181/37861182-2b7895c6-2f5a-11e8-8ea5-5fc7e817ad07.png)
Pushbullet (User Responding "Yes"):
Pushbullet (User Responding "No"):
