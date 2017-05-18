#!/usr/bin/python3
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse, Body, Media, Message
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

    # Convert message arguments to be url ready
    ready_message = convert_spaces(message)

    # Create API call
    # Only for Meme related calls
    if len(ready_message) < 3:
        for i in range(3 - len(ready_message)):
            ready_message.append("")
    meme_url = "http://apimeme.com/meme?meme={}&top={}&bottom={}".format(
        ready_message[0], ready_message[1], ready_message[2])

    # Responds with the meme with the img 
    msg = Message().body("Here is your {} meme".format(message[0])).media(meme_url)
    response.append(msg)

    return Response(str(response), mimetype="application/xml"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
