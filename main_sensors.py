# https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/
import sys

if not "win" in sys.platform: import RPi.GPIO as GPIO
import time

from ui.ui_input_sensor import InputSensorLevel
from config.config import GPIO_ULTRASONIC_TR_PIN, GPIO_ULTRASONIC_ECH_PIN, GPIO_REED_PIN_C1

if not "win" in sys.platform: 
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GPIO_ULTRASONIC_TR_PIN, GPIO.OUT)
    GPIO.setup(GPIO_ULTRASONIC_ECH_PIN, GPIO.IN)
    GPIO.setup(GPIO_REED_PIN_C1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(GPIO_REED_PIN_C2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(GPIO_REED_PIN_C3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

    def fetchReedSensorValues(main_instance):
        '''starting fetching reed sensor values'''
        # print("asda")
        # try:

        #     if topsenlvl.winfo_exists():
        #         sens.openEditor(main_instance, 1) # open editor toplevel window
        # except:
        #     print("except")

        if not "win" in sys.platform:
            SLEEP = .1
            flag1 = False
            flag2 = False
            flag3 = False
            while True:
                if GPIO.input(GPIO_REED_PIN_C1) == 0 and flag1 == False:
                    #if 
                    sens.openEditor(main_instance, 1) # open editor toplevel window
                    flag1 = True
                elif GPIO.input(GPIO_REED_PIN_C1) == 1 and flag1 == True:
                    flag1 = False

                # if GPIO.input(GPIO_REED_PIN_C2) == 0 and flag2 == False:
                #     #if 
                #     sens.openEditor(main_instance, 2) # open editor toplevel window
                #     flag2 = True
                # elif GPIO.input(GPIO_REED_PIN_C2) == 1 and flag2 == True:
                #     flag2 = False

                # if GPIO.input(GPIO_REED_PIN_C3) == 0 and flag3 == False:
                #     #if 
                #     sens.openEditor(main_instance, 1) # open editor toplevel window
                #     flag3 = True
                # elif GPIO.input(GPIO_REED_PIN_C3) == 1 and flag3 == True:
                #     flag3 = False                    
                time.sleep(SLEEP)
 
    def openEditor(main_instance, container_count):
        global topsenlvl
        topsenlvl = InputSensorLevel(main_instance, c_count=container_count) #parse instance to refresh textboxes



if __name__ == '__main__':
    try:
        while True:
            abstand = sens.ultraSonic()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)
 
    except KeyboardInterrupt:
        if not "win" in sys.platform: GPIO.cleanup()