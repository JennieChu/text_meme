#!/usr/bin/python3
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """
    Respond to incoming calls with a simple text message
    """

    resp = MessagingResponse()
    msg = Message().body("Hello, Mobile Monkey").media("https://demo.twilio.com/owl.png")
    resp.append(msg)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
