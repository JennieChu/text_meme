#!/usr/bin/python3
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse, Body, Media, Message
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from parsing_incoming import parse_inbound
from space_conversion import convert_spaces


app = Flask(__name__)

@app.route("/")
def check_app():
    # returns a simple string on success get
    return Response("It works!"), 200

@app.route("/twilio", methods=["POST"])
def inbound_sms():
    """
    Function that receives an SMS and returns necessary information
    """
    response = MessagingResponse()
    # Get the SMS message from the request
    inbound_message = request.form.get("Body")

    # Parse the response based on new lines or period,
    # Returns a list of arguments
    message = parse_inbound(inbound_message)

    # Opens the image, determine width & height for font resizing
    imgFile = "images" + message[0] + ".jpg"
    img = Image.open(imageFile)
    W, H = img.size

    # Variables for message and font
    msg_top = message[1]
    fontsize = 1
    img_fraction = 0.75

    draw = ImageDraw.Draw(img)

    # Loop to determine fontsize
    font = ImageFont.truetype("/Library/Font/Impact.ttf", fontsize)
    while font.getsize(msg)[0] < img_fraction*img.size[0]:
        fontsize += 1
        font = ImageFont.truetype("/Library/Font/Impact.ttf",fontsize)

    # Draw the new meme with given fontsize
    w, h = draw.textsize(msg, font)
    draw.text(((W - w) / 2, 0), msg, font=font)
    draw = ImageDraw.Draw(img)

    img.save("temporary_image.png")

    # Responds with the meme with the img 
    msg = Message().body("Here is your {} meme".format(message[0])).media("temporary_image.png")
    response.append(msg)

    return Response(str(response), mimetype="application/xml"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
