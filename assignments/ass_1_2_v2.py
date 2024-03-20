from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Constants
# Screen dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Font size
TEXT_HEIGHT = 8

# Breaking point
SCROLL_ROW = TEXT_HEIGHT + 2

# Bottom breaking point
BOTTOM_BREAK = int(SCREEN_HEIGHT - SCROLL_ROW / 2)


class Screen:
    def __init__(self):
        # The I2C bus, then planted to a variable
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.display = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, self.i2c)

    def draw_text(self, text):
        # Before drawing anything, scroll one row up
        self.display.scroll(0, SCROLL_ROW)
        # Clear first row
        self.display.fill_rect(0, 0, SCREEN_WIDTH, SCROLL_ROW, 0)
        # Clear bottom, or it looks ugly
        self.display.fill_rect(0, BOTTOM_BREAK, SCREEN_WIDTH, SCROLL_ROW, 0)

        self.display.text(text, 0, 0, 1)
        self.display.show()


oled = Screen()

while True:
    # Get input, code stands still while not getting anything
    input_text = input("Gib text: ")

    # Display new row of text from user
    oled.draw_text(input_text)
