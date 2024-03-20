from time import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Constants
# Screen dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Starting position for the dot on the y axis
START_POS = int(SCREEN_HEIGHT / 2)


class Screen:
    def __init__(self):
        # The I2C bus, then planted to a variable
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.display = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, self.i2c)


class Controller:
    def __init__(self):
        # Switches
        self.down = Pin(9, Pin.IN, Pin.PULL_UP)
        self.up = Pin(7, Pin.IN, Pin.PULL_UP)

        self.reset = Pin(8, Pin.IN, Pin.PULL_UP)

        self.position_x = 0
        self.position_y = START_POS

    # When pressing both, vector becomes -1 + 1 = 0 => going straight
    def input(self):
        if self.up() == 0 and self.position_y > 0:
            self.position_y -= 1
        if self.down() == 0 and self.position_y < SCREEN_HEIGHT - 1:
            self.position_y += 1

    def reset_position(self):
        self.position_x = 0
        self.position_y = START_POS


oled = Screen()
dot = Controller()

# Start out with a black screen
oled.display.fill(0)

while True:
    # Display a pixel on the current position
    oled.display.pixel(dot.position_x, dot.position_y, 1)
    oled.display.show()

    # Check for SW0 and SW2 input
    dot.input()

    # Increase x position by one every cycle
    # When reaching the end, go back to left
    dot.position_x = dot.position_x + 1 if dot.position_x < SCREEN_WIDTH else 0

    # Check if the player pressed the reset button
    if dot.reset() == 0:
        oled.display.fill(0)
        dot.reset_position()

    # gg go next frame
    sleep(0.01)
