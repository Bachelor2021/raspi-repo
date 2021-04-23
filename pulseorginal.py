#!/usr/bin/env python3.*
import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
myPWM = GPIO.PWM(18,50)
myPWM.start(10)
fps = 5
i = 0
Restget ="http://10.0.222.1:8000/RaspFPS"

while True:

    time.sleep(1)

    try:
    
        response = requests.get(Restget)
        data = response.json()
        
        fps_new = data['fps']
        start = data['start']
        fps = fps_new
        print(fps)

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
