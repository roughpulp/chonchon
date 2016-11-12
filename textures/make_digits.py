import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

width = 512
height = 512

img = Image.new("RGB", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("c:/Windows/Fonts/CalibriL.ttf", 150)

#for ii in range(4):
#    xx = (width / 4.0) * ii
#    draw.line([xx, 0, xx, 511], (255, 255, 255), 1)
#for ii in range(4):
#    yy = (height / 4.0) * ii
#    draw.line([0, yy, 511, yy], (255, 255, 255), 1)

for digit in range(10):
    xx = math.floor(digit % 4) * (width / 4.0) + (width / 18)
    yy = math.floor(digit // 4) * (height / 4.0)
    draw.text((xx, yy), str(digit), (255,255,255), font)

img.save("digits.png")

