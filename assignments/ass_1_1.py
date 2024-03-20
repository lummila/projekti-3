from time import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Constants
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
TEXT_WIDTH = 8
# The line where the UFO travels
BOTTOM_LINE = 50
START_POS_VERT = int(SCREEN_WIDTH / 2 - TEXT_WIDTH)


class Controller:
    def __init__(self):
        # Switches
        self.left = Pin(9, Pin.IN, Pin.PULL_UP)
        self.right = Pin(7, Pin.IN, Pin.PULL_UP)

        self.model = "<=>"
        self.width = TEXT_WIDTH * len(self.model)

        self.pos_x = START_POS_VERT
        self.pos_y = BOTTOM_LINE

    def move(self):
        if self.left() == 0 and self.pos_x > 0:
            self.pos_x -= 1

        if self.right() == 0 and self.pos_x < SCREEN_WIDTH - self.width:
            # print("Oikealla")
            self.pos_x += 1


class Screen:
    def __init__(self):
        # The I2C bus, then planted to a variable
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.display = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, self.i2c)

    def draw(self, ufo, pos_x, pos_y):
        self.display.fill(0)
        self.display.text(ufo, pos_x, pos_y, 1)
        self.display.show()


# Instance the UFO
ufo = Controller()
# Instance the screen controller
oled = Screen()

# Draw the player UFO at the start
oled.draw(ufo.model, ufo.pos_x, ufo.pos_y)

while True:
    # Current position
    ufo_pos = ufo.pos_x

    # Test for button input
    ufo.move()

    # If ufo.move() moved the ufo
    if ufo_pos != ufo.pos_x:
        oled.draw(ufo.model, ufo.pos_x, ufo.pos_y)

    # Clock cycle
    sleep(0.01)
