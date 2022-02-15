from PIL import Image, ImageDraw
from math import sqrt

# Main function, that uses recursion to draw every part of the snowflake
def koch(x1, y1, x2, y2, number_of_iterations, draw):

    """Draws a Koch snowflake with a number of desired iterations"""

    # Recursion ending condition
    if number_of_iterations > 0:
# Side 1
        koch(x1, y1, x1 + (x2 - x1) / 3, y1 + (y2 - y1) / 3, number_of_iterations - 1, draw)
# Side 2
        koch(x1 + (x2 - x1) / 3, y1 + (y2 - y1) / 3, (x1 + x2) / 2 + (y2 - y1) / (2 * sqrt(3)), \
        (y1 + y2) / 2 + (x1 - x2) / (2 * sqrt(3)), number_of_iterations - 1, draw)
# Side 3
        koch((x1 + x2) / 2 + (y2 - y1) / (2 * sqrt(3)), (y1 + y2) / 2 + (x1 - x2) / (2 * sqrt(3)), \
        x1 + (x2 - x1) * 2 / 3, y1 + (y2 - y1) * 2 / 3, number_of_iterations - 1, draw)
# Side 4
        koch(x1 + 2 *(x2 - x1) / 3, y1 + 2 *(y2 - y1) / 3, x2, y2, number_of_iterations - 1, draw)
    # If the number of iterations reaches zero, a line is drawn with current parameters
    else:
        draw.line((x1, y1, x2, y2), "black")

im = Image.new("RGB", (800, 650), color="white")
draw = ImageDraw.Draw(im)
LENGTH = 550
BASE_X = 100
BASE_Y = 160
iterations = int(input("Type your desired number of iterations (max. 6 recommended): "))

# Draws the upper side of the snowflake
koch(BASE_X, BASE_Y, LENGTH + BASE_X, BASE_Y, iterations, draw)

# Draws the right side of the snowflake
koch(BASE_X + LENGTH, BASE_Y, LENGTH/2 + BASE_X, BASE_Y + LENGTH * sqrt(3) / 2, iterations, draw)

# Draws the left side of the snowflake
koch(BASE_X + 0.5 * LENGTH, BASE_Y + LENGTH * sqrt(3) / 2, BASE_X, BASE_Y, iterations, draw)
im.show()