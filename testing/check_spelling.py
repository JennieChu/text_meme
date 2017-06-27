#!/usr/bin/python3

import enchant
from difflib import SequenceMatcher


def check_spelling(meme):
    """
    Spell checks the meme in the message and see if it matches any of the 
    available memes in our meme list.

    Return: If correct spelling is found or everything is spelled correctly, return True and word.
    Else, return False

    """

    word_list = enchant.request_pwl_dict("meme_list")
    meme_dict = enchant.DictWithPWL("en_US","meme_list")
    suggestions = meme_dict.suggest(meme)
    max_ratio = 0.0
    highest_word = ""

    for suggestion in suggestions:
        temp_ratio = similarity(meme, suggestion)
        if temp_ratio > max_ratio:
            highest_word = suggestion

    return(highest_word)


def similarity(a, b):
    """ Returns a ratio of how similar word b is to a"""
    return SequenceMatcher(None, a, b).ratio()

check_spelling("Bgi+Brid")
                
                
    
