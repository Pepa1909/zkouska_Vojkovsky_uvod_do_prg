from PIL import Image, ImageDraw
from math import sqrt
def koch(x1, y1, x2, y2, n, draw):
    if n > 0:
#Strana 1
        koch(x1, y1, x1 + (x2 - x1) / 3, y1 + (y2 - y1) / 3, n - 1, draw)
#Strana2
        koch(x1 + (x2 - x1) / 3, y1 + (y2 - y1) / 3, (x1 + x2) / 2 + (y2 - y1) / (2 * sqrt(3)), \
(y1 + y2) / 2 + (x1 - x2) / (2 * sqrt(3)), n - 1, draw)
#Strana 3
        koch((x1 + x2) / 2 + (y2 - y1) / (2 * sqrt(3)), (y1 + y2) / 2 + (x1 - x2) / (2 * sqrt(3)), \
        x1 + (x2 - x1) * 2 / 3, y1 + (y2 - y1) * 2 / 3, n - 1, draw)
# #Strana 4
        koch(x1 + 2 *(x2 - x1) / 3, y1 + 2 *(y2 - y1) / 3, x2, y2, n - 1, draw)
    else:
        draw.line((x1, y1, x2, y2), "black")

im = Image.new("RGB", (800, 650), color="white")
draw = ImageDraw.Draw(im)
d = 550
h = 1
koch(0 , 160, d, 160, h, draw)
# koch(100 + d, 160, 100 + 0.5 * d, 160 + d * sqrt(3) / 2, h, draw)
# koch(100 + 0.5 * d, 160 + d * sqrt(3) / 2, 100, 160, h, draw)
im.show()