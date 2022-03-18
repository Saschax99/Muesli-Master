import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
REED = 7
SLEEP = .1

GPIO.setup(REED, GPIO.IN)

while True:
    try:
        if GPIO.input(REED) == 1:
            print("An")
    except KeyboardInterrupt:
        exit()