from flask import Flask, render_template, redirect, url_for, request, jsonify, json
import board
import neopixel
numPixels = 10

desiredTemp = 72

pixels = neopixel.NeoPixel(board.D18, numPixels)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
   return "Hello world!"

@app.route('/changeColor', methods=['POST'])
def changeColor():
   data = request.get_json(force=True)
   red=data['red']
   blue=data['blue']
   green=data['green']
   pixels.fill((red,green,blue))



@app.route('/postTemp', methods=['POST'])
def postTemp():
  data = request.get_json(force=true)
  temp = data['temp']
  #return desired temp
  return desiredTemp

#Recieve temp info from particle
	#pi will send color info to particle if not based on temp

#

#


if __name__ == '__main__':
   app.run(host='0.0.0.0')
