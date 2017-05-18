#!/usr/bin/python3
"""
python program deploying site with list of available memes
"""
from collections import OrderedDict
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display():
    """
    return a website
    """
    with open('/home/ubuntu/text_meme/web_flask/meme_list') as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    content_url = OrderedDict()
    for i in content:
        new_url = "../static/images/memages/" + i
        content_url[new_url] = i.replace('+', ' ')

    return render_template("meme_check.html", content=content_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
