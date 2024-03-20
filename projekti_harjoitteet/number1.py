from time import sleep
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

button = Pin(9, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

oled = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

oled.fill(0)
oled.text("Hello world!", 0, 0, 1)
oled.show()

num = 0

while True:
    if button() == 0:
        num += 1
        if button() == 0:
            sleep(0.01)

        print("Painettu'd")
        oled.fill(0)
        oled.text(f"Button pressed\n{num} times!", 0, 0, 1)
        oled.show()
    sleep(0.05)
