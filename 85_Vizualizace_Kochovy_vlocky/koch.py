from PIL import Image, ImageDraw
from math import sqrt

# Main function, that uses recursion to draw every part of the snwoflake
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
length = 550
iterations = int(input("Zvolte úroveň Kochovy vločky (doporučená maximální úroveň je 6): "))

# Draws the upper side of the snowflake
koch(100, 160, length + 100, 160, iterations, draw)

# Draws the right side of the snowflake
koch(100 + length, 160, length/2 + 100, 160 + length * sqrt(3) / 2, iterations, draw)

# Draws the left side of the snowflake
koch(100 + 0.5 * length, 160 + length * sqrt(3) / 2, 100, 160, iterations, draw)
im.show()