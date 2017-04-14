#!/usr/bin/python3
"""
Functions to parse incoming text messages
"""
import sys
import re


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

    return (message)


if __name__ == "__main__":
    parse_inbound();
    
    
    
