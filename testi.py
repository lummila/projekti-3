from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

while True:
    try:
        led.toggle()
        sleep(1)
    except KeyboardInterrupt:
        print("Stopped")
        exit()
