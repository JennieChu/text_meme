#!/usr/bin/python3
from flask import Flask, Response, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse, Body, Media, Message
from parsing_incoming import parse_inbound
from space_conversion import convert_spaces
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import os
import requests

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
    account_sid = os.environ['account_sid']
    auth_token = os.environ['auth_token']

    client = Client(account_sid, auth_token)
    caller_ids = client.outgoing_caller_ids.list()

    response = MessagingResponse()
    # Get the SMS message from the request
    inbound_message = request.form.get("Body")
    
    # Gets the incoming SMS phone number
    inbound_number = request.form.get ("From")
    number_list = [caller.phone_number for caller in caller_ids]
    if  inbound_number not in number_list:
        msg = Message().body("Looks like you havent signed up for TextMeme. You can sign up via this link: http://34.210.213.199/sign_up.html#/")
    else:
        # Parse inbound message
        message = parse_inbound(inbound_message)
        meme = message[0]
        top = message[1]
        bot = message[2]

        # Check if meme exists, if not let user know
        if meme not in open('meme_list').read():
            msg = Message().body("That's not a meme. Check our our available memes here: INSERT").media("http://m.memegen.com/hxg2qb.jpg")
        else:
            # Responds with the meme with the img 
            url = 'http://34.210.213.199:8080/api/v1/get_image/' + meme + ':' + top + ':' + bot
            msg = Message().body("Here is your meme").media(url)
    
    response.append(msg)
    return Response(str(response), mimetype="application/xml"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
