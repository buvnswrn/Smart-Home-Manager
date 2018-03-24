import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
global stop
SR = 20
BEDROOM = 12
KITCHEN = 16
BATHROOM = 21
SR_LIGHT = 29
K_LIGHT = 11
H_LIGHT = 2
H_FAN = 3
H_MS = 4
H_TV =  17
BED_TV = 27
BED_FAN = 22
BED_LIGHT = 10
BATH_LIGHT = 9
GPIO.setup(SR, GPIO.IN)
GPIO.setup(KITCHEN, GPIO.IN)
GPIO.setup(BEDROOM, GPIO.IN)
GPIO.setup(BATHROOM, GPIO.IN)
GPIO.setup(SR_LIGHT, GPIO.OUT)
GPIO.setup(K_LIGHT, GPIO.OUT)
GPIO.setup(H_FAN, GPIO.OUT)
GPIO.setup(H_LIGHT, GPIO.OUT)
GPIO.setup(H_MS, GPIO.OUT)
GPIO.setup(H_TV, GPIO.OUT)
GPIO.setup(BED_FAN, GPIO.OUT)
GPIO.setup(BED_LIGHT, GPIO.OUT)
GPIO.setup(BED_TV, GPIO.OUT)
GPIO.setup(BATH_LIGHT, GPIO.OUT)


def isSensorOn(requirements):
    storeroom=split(requirements,"SR")
    kitchen=split(requirements,"KT")
    bathroom=split(requirements,"BR")
    bedroom=split(requirements,"BED")
    while True:
        if GPIO.input(SR):
            for req in storeroom:
                if(req=="Light"):
                    GPIO.output(SR_LIGHT,GPIO.HIGH)
        if GPIO.input(KITCHEN):
            for req in kitchen:
                
        if GPIO.input(BEDROOM):
            for req in bedroom:
                switch
        if GPIO.input(BATHROOM):
            for req in bathroom:
                switch


