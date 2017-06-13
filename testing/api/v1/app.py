#!/usr/bin/python3
from PIL import Image, ImageDraw
from io import StringIO
from io import BytesIO
from flask import Flask, render_template, jsonify, send_file
import json

app = Flask(__name__)

@app.route('/api/v1/get_image', methods=['GET','POST'],
           strict_slashes=False)
def get_image():
    """ Returns an image given id """
    image = Image.new("RGB", (100, 100))
    draw = ImageDraw.Draw(image)

    byte_io = BytesIO()
    image.save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

def serve_pil_image(pil_path):
    img_io = BytesIO()
#    pil_image = Image.open(pil_path)
    pil_image.save(img_io, 'PNG', quality=70)
#    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')
