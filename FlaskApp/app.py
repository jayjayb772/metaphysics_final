from flask import Flask, render_template, redirect, url_for, request, jsonify, json

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
   neopixel.setColor(red,blue,green)


if __name__ == '__main__':
   app.run(host=0.0.0.0)
