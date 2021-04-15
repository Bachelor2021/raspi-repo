import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
myPWM = GPIO.PWM(18,50)
myPWM.start(10)
fps = 5
i = 0

while True:

    time.sleep(2)

    try:
    
        

        myPWM.ChangeDutyCycle(50)
        myPWM.ChangeFrequency(int(fps))

        
        # if int(fps_new)==0:
        #     myPWM.ChangeDutyCycle(0)
        #     if i%100==0:
        #         print("1")
               
        # elif int(fps_new)!= fps:
        #     fps = int(fps_new)
        #     myPWM.ChangeDutyCycle(50)
        #     myPWM.ChangeFrequency(int(fps))
        # elif fps==int(fps_new) and i%100==0:
           
        #     myPWM.ChangeDutyCycle(50)
        #     myPWM.ChangeFrequency(int(fps))
        

                
        
        
        
    except Exception as e:

        myPWM.ChangeDutyCycle(0)
       

GPIO.cleanup()