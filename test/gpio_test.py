import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

GPIO.output(40, GPIO.LOW)
sleep(1)
GPIO.output(40, GPIO.HIGH)
sleep(1)
GPIO.output(40, GPIO.LOW)
sleep(1)
GPIO.output(40, GPIO.HIGH)
sleep(1)
GPIO.output(40, GPIO.LOW)
sleep(1)
GPIO.output(40, GPIO.HIGH)
sleep(1)

GPIO.cleanup()	
