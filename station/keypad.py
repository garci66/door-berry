import RPi.GPIO as GPIO
import time
import os
from threading import Timer

class RaspiBoard():

    IN1=4
#    IN2=22
#    IN3=4
    OUT1=23
    OUT2=24

    def __init__(self):
        '''
        Constructor        '''
#        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.IN)
        GPIO.setup(self.OUT1, GPIO.OUT)
        GPIO.setup(self.OUT2, GPIO.OUT)
	GPIO.output(self.OUT1,True)
	GPIO.output(self.OUT2,True)
	print "Setting up GPIO DONE"

#        GPIO.setup(self.IN2, GPIO.IN)
#        GPIO.setup(self.IN3, GPIO.IN)

    def destroy(self):
        GPIO.cleanup()
    
    def keyPressed(self):
        if(GPIO.input(self.IN1) == True): return 1
 #       if(GPIO.input(self.IN2) == True): return 2
 #       if(GPIO.input(self.IN3) == True): return 3
        return 0

    def setOut(self, output, value):
#	print  output, value
        if(output==1):
           GPIO.output(self.OUT1,not value)
        elif(output==2):
           GPIO.output(self.OUT2,not value)

    def setTimedOutput(self, output, value, duration):
        self.setOut(output,value)
        Timer(duration,self.setOut,[output, not value]).start()




