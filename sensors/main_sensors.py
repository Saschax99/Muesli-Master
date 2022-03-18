# https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/
import sys
if not "win" in sys.platform: import RPi.GPIO as GPIO
import time
from config.config import GPIO_ULTRASONIC_TR_PIN, GPIO_ULTRASONIC_ECH_PIN, GPIO_REED_PIN
# from ui.ui_input_sensor import InputSensorLevel CIRCULATING ISSUE

if not "win" in sys.platform: 
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GPIO_ULTRASONIC_TR_PIN, GPIO.OUT)
    GPIO.setup(GPIO_ULTRASONIC_ECH_PIN, GPIO.IN)
    GPIO.setup(GPIO_REED_PIN, GPIO.IN)

class sens:
    '''configured sensors'''

    def ultraSonic(self):
        '''get distance of ultra sonic sensor'''
        if not "win" in sys.platform: 
            GPIO.output(GPIO_ULTRASONIC_TR_PIN, True) # set Trigger to HIGH
            time.sleep(0.00001) # set Trigger after .001ms to LOW
            GPIO.output(GPIO_ULTRASONIC_TR_PIN, False)
    
        start = time.time()
        stop = time.time()
        if not "win" in sys.platform:
            while GPIO.input(GPIO_ULTRASONIC_ECH_PIN) == 0: # save start time
                start = time.time()

            while GPIO.input(GPIO_ULTRASONIC_ECH_PIN) == 1: # save stop time after triggered echo
                stop = time.time()
    
        TimeElapsed = stop - start # time diff. between these two times
        distance = (TimeElapsed * 34300) / 2 # multiplicate with sonic speed (34300 cm/s) and div. with 2 because the way there and back from the sensor
        if not "win" in sys.platform: GPIO.cleanup() # clean gpios
        return distance

    def fetchReedSensorValues():
        '''starting fetching reed sensor values'''
        sens.openEditor(1)
        c1_callback = False
        if not "win" in sys.platform:
            while True:
                try:
                    if GPIO.input(GPIO_REED_PIN) == GPIO.HIGH and c1_callback:
                        print("true sensor")
                        sens.openEditor()
                        c1_callback = True
                        # OPEN CONTAINER 1 INPUT WINDOW AND ONLY ACCEPT BUTTON
                except KeyboardInterrupt:
                    exit()
 
    def openEditor(container_count):
        #InputSensorLevel(c_count=container_count) #parse instance to refresh textboxes
        pass


if __name__ == '__main__':
    try:
        while True:
            abstand = sens.ultraSonic()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)
 
    except KeyboardInterrupt:
        if not "win" in sys.platform: GPIO.cleanup()