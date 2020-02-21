# add comment here, charlie,
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
led0=26
led1=19
led2=13
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(led0, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

def blink(pin,sec): 
   GPIO.output(pin, GPIO.HIGH) # Turn on
   sleep(sec) # Sleep for 1 second
   GPIO.output(pin, GPIO.LOW) # Turn off
   sleep(sec) # Sleep for 1 second


while True: # Run forever
  blink(led0,1)
  blink(led1,2)
  blink(led2,3)
  