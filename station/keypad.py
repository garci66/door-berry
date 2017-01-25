import RPi.GPIO as GPIO
import time
import os
from threading import Timer

class RaspiBoard():

    IN1=4  #Doorbell
    IN2=27 #Magnetic Sensor for gate
#    IN3=4
    OUT1=23 #Relay 1
    OUT2=24 #Relay 2 (probablt not used)
    OUT3=17 #LED
    lastKey=0

    def __init__(self):
        '''
        Constructor        '''
#        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.IN)
        GPIO.setup(self.IN2, GPIO.IN)
        GPIO.setup(self.OUT1, GPIO.OUT,initial=True) #Set initial value to high - Inverting relay
        GPIO.setup(self.OUT2, GPIO.OUT,initial=True)
        GPIO.setup(self.OUT3, GPIO.OUT)

	GPIO.output(self.OUT1,True)
	GPIO.output(self.OUT2,True)
	GPIO.output(self.OUT3,False)
	
	print "Setting up GPIO DONE"


    def destroy(self):
        GPIO.cleanup()
    
    def keyPressed(self):
        if(GPIO.input(self.IN1) == False): return 1
        return 0

    def gateOpen(self):
        return GPIO.input(self.IN2)


    def setOut(self, output, value):
#	print  output, value
        if(output==1):
           GPIO.output(self.OUT1,not value) #Relays are inverting
        elif(output==2):
           GPIO.output(self.OUT2,not value)
        elif(outut==3):
           GPIO.output(self.OUT3,value) #The LED is not inverting

    def setTimedOutput(self, output, value, duration):
        self.setOut(output,value)
        Timer(duration,self.setOut,[output, not value]).start()




