import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
trigger =7
echo =12
led=8

GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trigger,0)

time.sleep(0.1)

pwm=GPIO.PWM(led,100)

dc=0
pwm.start(dc)

print("distance: ")

def distCalc():
    GPIO.output(trigger,1)
    time.sleep(0.00001)
    GPIO.output(trigger,0)
    while GPIO.input(echo)==0:
        pass
    start=time.time()
    while GPIO.input(echo)==1:
        pass
    end=time.time()
    
    dist=(end-start)*20000
    return dist
while True:
    dist=distCalc()
    print(dist)
    
    
    if dist>40:
        GPIO.output(led,GPIO.HIGH)
        pwm.ChangeDutyCycle(0)
    else:
        pwm.ChangeDutyCycle(100-(dist*2))
        GPIO.output(led,GPIO.LOW)
pwm.stop()
GPIO.cleanup()
