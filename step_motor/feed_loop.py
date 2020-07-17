import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#control_pins = [7,11,13,15]
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


meal_time = '20:44', '20:40', '20:42'


while(1):
    current_time = time.strftime('%H:%M', time.localtime(time.time()))
    
    if current_time in meal_time:
        print("meal time : " + current_time)
        for i in range(10):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)
    else:
        print("no match  : " + current_time)
        
    time.sleep(60)
