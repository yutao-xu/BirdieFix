# import RPi.GPIO as GPIO
import time

def open_door():
    RELAY_PIN = 12

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)

    GPIO.setup(RELAY_PIN, GPIO.OUT)

    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(RELAY_PIN, GPIO.LOW)
    time.sleep(1)