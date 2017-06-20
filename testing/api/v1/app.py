#!/usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
from io import StringIO
from io import BytesIO
from flask import Flask, render_template, jsonify, send_file
import json
import requests
import os

app = Flask(__name__)

@app.route('/add_number/<number>', methods=['GET', 'POST'], strict_slashes=False)
def add_number(number):
    account_sid = os.environ['account_sid']
    auth_token = os.environ['auth_token']
    url = 'https://'+ account_sid + ':' + auth_token + '@api.twilio.com/2010-04-01/Accounts/'+ account_sid + '/OutgoingCallerIds'
    data = {'PhoneNumber': number}
    r = requests.post(url, data = data)
    print(r.text)
    return r.text

@app.route('/api/v1/get_image/<meme>:<top>:<bottom>', methods=['GET','POST'],
           strict_slashes=False)
def get_image(meme, top="", bottom=""):
    """ Create and returna an image with placed text"""
    image = create_image(meme, top, bottom)
    byte_io = BytesIO()
    image.save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

def create_image(meme, top, bottom):
    """ Create and return the selected meme"""

    # Checks if top or bottom contained no strings
    if top == "NONEMSG":
        top = " "
    else:
        top = top.replace("_", " ")
    if bottom == "NONEMSG":
        bottom = " "
    else:
        bottom = bottom.replace("_", " ")

    # Opens image to check
    imageFile = '../../../web_flask/static/images/memages/' + meme
    image = Image.open(imageFile)
    draw = ImageDraw.Draw(image)

    # Create text on top of image
    W, H = image.size
    fontsize = 1
    img_fraction = 0.75

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/impact.ttf", fontsize)
    while font.getsize(top)[0] < img_fraction*image.size[0]:
        fontsize += 1
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/impact.ttf", fontsize)

    bot_fontsize = 1
    bot_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/impact.ttf", bot_fontsize)
    while bot_font.getsize(bottom)[0] < img_fraction*image.size[0]:
        bot_fontsize += 1
        bot_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/impact.ttf", bot_fontsize)

    # Resize font if too large
    if fontsize > 100:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/impact.ttf", 75)
    if bot_fontsize > 90:
        bot_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/impact.ttf", 75)

    # Draws the image
    w, h = draw.textsize(top, font)
    b_w, b_h = draw.textsize(bottom, bot_font)
    draw.text(((W-w)/2, 0), top, font=font)
    draw.text(((W-b_w)/2, (H-b_h)), bottom, font=bot_font)
    draw = ImageDraw.Draw(image)

    print("HELLO")

    return (image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')
