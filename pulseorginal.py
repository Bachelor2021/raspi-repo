
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

    time.sleep(2)

    try:
    
        response = requests.get(Restget)
        data = response.json()
        
        fps_new = data['fps']
        start = data['start']
        fps = fps_new
        
        if int(fps)==0:
            myPWM.ChangeDutyCycle(0)
        else:
            myPWM.ChangeDutyCycle(50)
            myPWM.ChangeFrequency(int(fps))

        
       

                
        
        
        
    except Exception as e:

        myPWM.ChangeDutyCycle(0)
       

GPIO.cleanup()
