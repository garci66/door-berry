import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT,initial=True)
GPIO.setup(24, GPIO.OUT)


GPIO.output(23,True)
GPIO.output(24,True)



