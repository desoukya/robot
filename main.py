#ENB => RIGHT SIDE
#ENA => LEFT SIDE

import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

# All Wheels Turn Forwards
def forward(tf):
    init()
   
    # GPIO 15 => IN1 => OUT1 => ENB
    gpio.output(15, True)
 
    # GPIO 13 => IN2 => OUT2 => ENB
    gpio.output(13, False)

    # GPIO 11 => IN3 => OUT3 => ENA
    gpio.output(11, True)

    # GPIO 7 => IN4 => OUT4 => ENA
    gpio.output(7, False)
    
    time.sleep(tf)
    gpio.cleanup()

# All Wheels Turn Backwards
def reverse(tf):
    init()

    # GPIO 15 => IN1 => OUT1 => ENB
    gpio.output(15, False)

    # GPIO 13 => IN2 => OUT2 => ENB
    gpio.output(13, True)

    # GPIO 11 => IN3 => OUT3 => ENA
    gpio.output(11, False)

    # GPIO 7 => IN4 => OUT4 => ENA
    gpio.output(7, True)

    time.sleep(tf)
    gpio.cleanup()

# Right Wheels Turn Forward
def left(tf):
    init()

    # GPIO 15 => IN1 => OUT1 => ENB
    gpio.output(15, True)

    # GPIO 13 => IN2 => OUT2 => ENB
    gpio.output(13, False)

    # GPIO 11 => IN3 => OUT3 => ENA
    gpio.output(11, False)

    # GPIO 7 => IN4 => OUT4 => ENA
    gpio.output(7, False)

    time.sleep(tf)
    gpio.cleanup()      

# Left Wheels Move Forward
def right(tf):
    init()

    # GPIO 15 => IN1 => OUT1 => ENB
    gpio.output(15, False)

    # GPIO 13 => IN2 => OUT2 => ENB
    gpio.output(13, False)

    # GPIO 11 => IN3 => OUT3 => ENA
    gpio.output(11, True)

    # GPIO 7 => IN4 => OUT4 => ENA
    gpio.output(7, False)

    time.sleep(tf)
    gpio.cleanup()

# Right Wheels Turn Forward
# Left Wheels Turn Backward
def pivot_right(tf):
    init()

    # GPIO 15 => IN1 => OUT1 => ENB
    gpio.output(15, True)

    # GPIO 13 => IN2 => OUT2 => ENB
    gpio.output(13, False)

    # GPIO 11 => IN3 => OUT3 => ENA
    gpio.output(11, False)

    # GPIO 7 => IN4 => OUT4 => ENA
    gpio.output(7, True)

    time.sleep(tf)
    gpio.cleanup()

# Right Wheels Turn Backward
# Left Wheels Turn Forward
def pivot_left(tf):
    init()

    # GPIO 15 => IN1 => OUT1 => ENB
    gpio.output(15, False)

    # GPIO 13 => IN2 => OUT2 => ENB
    gpio.output(13, True)

    # GPIO 11 => IN3 => OUT3 => ENA
    gpio.output(11, True)

    # GPIO 7 => IN4 => OUT4 => ENA
    gpio.output(7, False)

    time.sleep(tf)
    gpio.cleanup()

#forward(3)
#reverse(3)
#left(2)
#right(2)
pivot_right(3)
pivot_left(3)
