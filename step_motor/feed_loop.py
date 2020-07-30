import RPi.GPIO as GPIO
import time


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


meal_time = '13:59','14:00', '14:01', '14:02'


while(1):
    current_time = time.strftime('%H:%M', time.localtime(time.time()))
    GPIO.setmode(GPIO.BCM)
    control_pins = [12,16,20,21]
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    
    if current_time in meal_time:
        print("meal time : " + current_time)
#for i in range(170):
        for i in range(30):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)
    else:
        print("no match  : " + current_time)

    GPIO.cleanup()
    time.sleep(60)
