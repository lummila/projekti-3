from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

cycle = 0
while cycle < 5:
    try:
        led.toggle()
        sleep(1)
        cycle += 1
    except KeyboardInterrupt:
        print("Stopped")
        quit()

led.off()
