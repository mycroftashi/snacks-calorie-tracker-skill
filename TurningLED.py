import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
print "LED on Green"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)
print "LED on Orange"
GPIO.output(23,GPIO.HIGH)
time.sleep(10)
print "LED off"
GPIO.output(23,GPIO.LOW)