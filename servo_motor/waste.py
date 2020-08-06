import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12,50)

p.start(0)

p.ChangeDutyCycle(2.5)
sleep(3)

p.ChangeDutyCycle(7.5)
sleep(1)

p.stop()

GPIO.cleanup()
