#ENB => RIGHT SIDE
#ENA => LEFT SIDE

import RPi.GPIO as gpio
import time
import sys
import Tkinter
import termios
import tty

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

# All Wheels Turn Forwards
def forward(tf):
    #init()
   
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
    #init()

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
    #init()

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
    #init()

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
    #init()

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
    #init()

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



# Register Keyboard Inputs
def key_input(e):
    init()
    print ("Key:", e.char)
    key = e.char
    stime = 0.030    # sleep time
  
    if   (key.lower() == 'e'):
          forward(stime)
    elif (key.lower() == 'd'):
          reverse(stime)
    elif (key.lower() == 's'):
          left(stime)
    elif (key.lower() == 'f'):
          right(stime)
    elif (key.lower() == 'w'):
          pivot_left(stime)
    elif (key.lower() == 'r'):
          pivot_right(stime)

    gpio.cleanup()


# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    init()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        print("Enter Command")
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    key = getch()
    stime = 0.030
    if   (key.lower() == 'e'):
          forward(stime)
    elif (key.lower() == 'd'):
          reverse(stime)
    elif (key.lower() == 's'):
          left(stime)
    elif (key.lower() == 'f'):
          right(stime)
    elif (key.lower() == 'w'):
          pivot_left(stime)
    elif (key.lower() == 'r'):
          pivot_right(stime)
    elif (key.lower() == 'x'):
          break

    gpio.cleanup()

#cmd = Tkinter.Tk()
#cmd.bind('<KeyPress>', key_input)
#cmd.mainloop()

#init()
#forward(3)
#reverse(3)
#left(2)
#right(2)
#pivot_right(3)
#pivot_left(3)
