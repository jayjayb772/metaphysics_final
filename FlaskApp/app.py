from flask import Flask, render_template, redirect, url_for, request, jsonify, json
import board
import neopixel
numPixels = 10
pixels = neopixel.NeoPixel(board.D18, numPixels)

app = Flask(__name__)

@app.route('/')
def mainPage():
   return "Hello world!"

@app.route('/changeColor', methods=['POST'])
def changeColor():
   data = request.get_json(force=True)
   red=data['red']
   blue=data['blue']
   green=data['green']
   pixels.fill((red,green,blue))


if __name__ == '__main__':
   app.run(host='0.0.0.0')
