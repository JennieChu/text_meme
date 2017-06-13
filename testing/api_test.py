#!/usr/bin/python3
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse, Body, Media, Message
from parsing_incoming import parse_inbound
from space_conversion import convert_spaces
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
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
    response = MessagingResponse()
    # Get the SMS message from the request
    inbound_message = request.form.get("Body")


    # Responds with the meme with the img 
    msg = Message().body("Here is your meme").media('http://localhost:8080/api/v1/get_image')
#    response.append(Message().body("HMM"))
    response.append(msg)
    print("hmmmm")
    return Response(str(response), mimetype="application/xml"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
