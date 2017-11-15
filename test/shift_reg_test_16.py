import RPi.GPIO as GPIO
import sys
from time import sleep


SERIAL = 3
CLOCK = 5
CLEAR = 8
LATCH = 7

parks = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13], sys.argv[14], sys.argv[15], sys.argv[16]]

print(parks)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERIAL, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)
GPIO.setup(CLEAR, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT)


for i in parks:
	GPIO.output(SERIAL,int(i))
	sleep(0.01)
	GPIO.output(CLOCK,1)
	sleep(0.01)
	GPIO.output(CLOCK,0)
	sleep(0.01)
GPIO.output(LATCH,1)
sleep(0.01)
GPIO.output(LATCH,0)
sleep(0.1)

