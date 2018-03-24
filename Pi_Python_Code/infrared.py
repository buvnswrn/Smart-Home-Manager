import RPi.GPIO as GPIO
import time
from time import sleep
import Notify as notify
import multiprocessing
class Monitor:
    intruder=None
    def __init__(self):
        self._running=True
    def terminate(self):
        self._running=False
    def run(self):
        GPIO.setmode(GPIO.BCM)
        global intruder
        SR = 14
        KITCHEN = 18
        BEDROOM = 23
        PORCH = 24
        PORCH_MOTION = 25
        GPIO.setup(SR, GPIO.IN)
        GPIO.setup(KITCHEN, GPIO.IN)
        GPIO.setup(BEDROOM, GPIO.IN)
        GPIO.setup(PORCH, GPIO.IN)
        GPIO.setup(PORCH_MOTION, GPIO.IN)
        try:
            time.sleep(2)
            while self._running:
                intruder=None
                if not GPIO.input(PORCH_MOTION) and GPIO.input(PORCH):
                    print("Porch")
                    intruder="Porch"
                if GPIO.input(SR):
                    print("Store Room")
                    intruder="Store Room"
                if not GPIO.input(KITCHEN):
                    print("Kitchen")
                    intruder="Kitchen"
                if not GPIO.input(BEDROOM):
                    intruder="Bedroom"
                    print("Bedroom")
                if intruder is not None:
                    notify.notify_neighbor("Bhuvaneshwaran")
                    notify.notifyuser_place(intruder)
                    sleep(5)
        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()


c=Monitor()
c.run()
