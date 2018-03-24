# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import face_recognition as fr
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
SEC_PIR=8
u=0
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(SEC_PIR,GPIO.IN)
count=0
try:
       print("PIR Module Test (CTRL+C to exit)")
       time.sleep(2)
       print("Ready")
       while True:
              if GPIO.input(PIR_PIN):
                     print("Motion Detected in Bedroom!",count)
                     count+=1
              if GPIO.input(SEC_PIR):
                     print("Motion Detected in Hall!",count)
                     count+=1
              if GPIO.input(PIR_PIN) and GPIO.input(SEC_PIR) and u==0:
                     u+=1
                     fr.recognise()
              else:
                     print("No Motion")
              time.sleep(1)
except KeyboardInterrupt:
       print("Quit")
       GPIO.cleanup()
