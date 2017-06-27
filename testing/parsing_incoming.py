#!/usr/bin/python3
"""
Functions to parse incoming text messages
"""
import sys
from check_spelling import check_spelling


def parse_inbound(message):
    """
      Parses an inbound messages
    """
    # Splits message based on new lines or periods
    message = message.replace('\n', '.')
    message = message.split('.')

    # Capitalize first letter of each word for meme
    message[0] = message[0].title()
    message[0] = message[0].replace(" ", "+")

    # Checks spelling errors in meme
    if message[0] != "Start":
        message[0] = check_spelling(message[0])

    # Connect messages for api
    try:
        message[1] = message[1].replace(" ", "_")
        if message[1] == "":
            message[1] = "NONEMSG"
    except:
        message.append("NONEMSG")
    try:
        message[2] = message[2].replace(" ", "_")
        if message[2] ==  "":
            message[2] = "NONMSG"
    except:
        message.append("NONEMSG")

    return message

    # Removes empty element
    if message[-1] is "":
        del message[-1]


if __name__ == "__main__":
    parse_inbound();
    
    
    
