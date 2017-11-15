import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time                             # calling for time to provide delays in program

IO.setwarnings(False)           # do not show any warnings
x=1                

CLOCK = 5
SERIAL = 3
LATCH = 7
CLEAR = 8


IO.setmode (IO.BOARD)        # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
IO.setup(SERIAL,IO.OUT)            # initialize GPIO Pins as an output.
IO.setup(CLOCK, IO.OUT)
IO.setup(LATCH, IO.OUT)
IO.setup(CLEAR, IO.OUT)

IO.setup(CLEAR, 0)
time.sleep(0.1)
IO.setup(CLEAR, 1)
while 1:                               # execute loop forever
    for y in range(8):            # loop for counting up 8 times
        IO.output(SERIAL,1)            # pull up the data pin for every bit.
        time.sleep(0.1)            # wait for 100ms
        IO.output(CLOCK,1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(CLOCK,0)            # pull CLOCK pin down, to send a rising edge
        IO.output(SERIAL,0)            # clear the DATA pin
        IO.output(LATCH,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(LATCH,0)            # pull down the SHIFT pin
    for y in range(8):            # loop for counting up 8 times
        IO.output(SERIAL,0)            # clear the DATA pin, to send 0
        time.sleep(0.1)            # wait for 100ms
        IO.output(CLOCK,1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(CLOCK,0)            # pull CLOCK pin down, to send a rising edge
        IO.output(SERIAL,0)            # keep the DATA bit low to keep the countdown
        IO.output(LATCH,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(LATCH,0)
