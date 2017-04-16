#!/usr/bin/python3
"""
Functions to parse incoming text messages
"""
import sys


def parse_inbound(message):
    """
      Parses an inbound messages
    """
    # Splits message based on new lines or periods
    message = message.replace('\n', '.')
    message = message.split('.')

    # Capitalize first letter of each word for meme
    message[0] = message[0].title()

    # Removes empty element
    if message[-1] is "":
        del message[-1]

    # Determine type of user request
    if "help" in message[0]:
        request = "HELP"
    elif "available" in message[0]:
        request = "AVAIL"
    else:
        request = "MEME"

    return request, message


if __name__ == "__main__":
    parse_inbound();
    
    
    
