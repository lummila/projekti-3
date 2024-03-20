from time import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Constants
# Screen dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Font size
TEXT_WIDTH = 8
TEXT_HEIGHT = 8

# Breaking point
HEIGHT_LIMIT = SCREEN_HEIGHT - TEXT_HEIGHT * 3


class Screen:
    def __init__(self):
        # The I2C bus, then planted to a variable
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.display = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, self.i2c)

        self.displayed_text = []

    # Takes input, sees if it can fit to the screen, then draws
    def take_text(self, text):
        text_pos_y = len(self.displayed_text) * TEXT_HEIGHT

        if text_pos_y > HEIGHT_LIMIT:
            self.displayed_text.pop(0)

        self.displayed_text.append(text)

    # Goes through text list and displays all the inputs
    def draw_text(self):
        self.display.fill(0)

        # The y position limit is already calculated in take_text()
        text_position = 0

        for text in self.displayed_text:
            self.display.text(text, 0, text_position, 1)
            self.display.show()

            text_position += TEXT_HEIGHT + 2


oled = Screen()

while True:
    # Get input, code stands still while not getting anything
    input_text = input("Gib text: ")

    oled.take_text(input_text)
    oled.draw_text()
