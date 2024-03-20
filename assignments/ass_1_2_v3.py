from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Constants
# Screen dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Font size

TEXT_HEIGHT = 8

# Bottom breaking point
BOTTOM_BREAK = int(SCREEN_HEIGHT - SCROLL_ROW / 2)

# One row
ROW = TEXT_HEIGHT + 2
# Last row
LAST_ROW = ROW * 5


class Screen:
    def __init__(self):
        # The I2C bus, then planted to a variable
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.display = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, self.i2c)

        # Row counter
        self.scroll_row = 0

    def draw_text(self, text):
        if self.scroll_row < (TEXT_HEIGHT + 2) * 6:
            self.display.text(text, 0, self.scroll_row, 1)

            self.scroll_row += ROW
        else:
            self.display.scroll(0, -ROW)
            self.display.fill_rect(0, LAST_ROW, SCREEN_WIDTH, ROW, 0)
            self.display.text(text, 0, LAST_ROW, 1)
        self.display.show()


oled = Screen()

while True:
    # Get input, code stands still while not getting anything
    input_text = input("Gib text: ")

    # Display new row of text from user
    oled.draw_text(input_text)
