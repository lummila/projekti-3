from time import sleep
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

button = Pin(9, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

oled = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

oled.fill()
