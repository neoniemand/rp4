import RPi.GPIO as GPIO
import time
import subprocess

PIR_PIN = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

while(1):
    current_time = time.strftime('%H:%M', time.localtime(time.time()))
    
    if GPIO.input(PIR_PIN):
        print("meal time : " + current_time)
        subprocess.call(["/home/pi/rp4/step_motor/feed.sh"])
        print("sleep 10")
        time.sleep(10)
    else:
        print("no match  : " + current_time)

    time.sleep(0.5)

GPIO.cleanup()
