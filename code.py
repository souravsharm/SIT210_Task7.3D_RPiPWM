import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 12
led = 16
buzz = 23

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzz,GPIO.OUT)

GPIO.output(led,GPIO.LOW)
GPIO.output(buzz, False)
def get_distance():

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO) == False:
    st = time.time()

  while GPIO.input(ECHO) == True:
    et = time.time()

  signal = et-st
  distance = signal / 0.000058 #in centimeters

  return distance

def buzzer_intensity(x):
    GPIO.output(buzz, True)
    time.sleep(x)
    GPIO.output(buzz, False)
    time.sleep(x)

def led_intensity(y):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(y)
    GPIO.output(led, GPIO.LOW)
    time.sleep(y)

while True:
    distance = get_distance()
    time.sleep(0.05)
    print(distance)
    
    if ( distance < 15 and distance >= 11 ):
        buzzer_intensity(0.3)
        led_intensity(0.3)
    
    if ( distance < 11 and distance >=7 ):
        buzzer_intensity(0.1)
        led_intensity(0.1)
    
    if ( distance < 7 ):
        GPIO.output(buzz, True)
        GPIO.output(led, GPIO.HIGH)