#!/usr/bin/python3
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

imageFile = "images/willy-wonka.jpg"
im1=Image.open(imageFile)
W, H = im1.size
msg = "So you think HTML and CSS is a language"
fontsize = 1
img_fraction = 0.75
draw = ImageDraw.Draw(im1)

font = ImageFont.truetype("/Library/Fonts/Impact.ttf", fontsize)
while font.getsize(msg)[0] < img_fraction*im1.size[0]:
    fontsize += 1
    font = ImageFont.truetype("/Library/Font/Impact.ttf", fontsize)


w, h = draw.textsize(msg, font)
draw.text(((W-w)/2, 0), msg, font=font)
draw = ImageDraw.Draw(im1)

im1.save("marked_image.png")
