import RPi.GPIO as GPIO
import time
import db
import face_recognition as fr
GPIO.setmode(GPIO.BCM)
HALL_SENSOR1 = 7
HALL_SENSOR2 = 8
H_LIGHT = 2
H_FAN = 3
H_MS = 4
H_TV =  17
port=[{"Fan":3,"Light":2,"Tv":17,"Music_System":4}]
GPIO.setup(H_FAN, GPIO.OUT)
GPIO.setup(H_LIGHT, GPIO.OUT)
GPIO.setup(H_MS, GPIO.OUT)
GPIO.setup(H_TV, GPIO.OUT)
u=0
GPIO.setup(HALL_SENSOR1, GPIO.IN)
GPIO.setup(HALL_SENSOR2,GPIO.IN)
count=0
try:
    while True:
        if GPIO.input(HALL_SENSOR1) and GPIO.input(HALL_SENSOR2):
            u+=1
            name=fr.recognise()
            key_list={'Fan','Light','Modem','TV','Music_System'}
            needlist=db.fetch(name,key_list,1)
            for r in needlist:
                for key in port:
                    if key[r] is not None:
                       print(key[r],type(key[r]))
                       GPIO.output(item,GPIO.HIGH)
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()