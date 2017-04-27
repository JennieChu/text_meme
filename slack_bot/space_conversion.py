#!/usr/bin/env python3
"""
Function to convert spaces to plus signs to get ready for
api call
"""

def convert_spaces(msg_list):
    """
    Converts each argument of the message such that all spaces
    are replaced by plus signs
    """
    new_list = []
    for str in msg_list:
        new_list.append(str.replace(' ', '+'))
    return (new_list)


if __name__ == "__main__":
    convert_spaces()
