import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin = 7

GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

while True:
    if GPIO.input(pirPin) == GPIO.LOW:
        print("No motion")
    else:
        print("Motion detected !!")
        print("sleep !!")
        time.sleep(5)
        print("wake up !!")
    time.sleep(0.1)
