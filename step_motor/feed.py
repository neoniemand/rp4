import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
control_pins = [12,16,20,21]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

#for i in range(170):
for i in range(82):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.002)
GPIO.cleanup()
