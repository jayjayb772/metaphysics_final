import EasyLCD as lcd
import requests

mylcd = lcd.mylcd

baseURL = "http://0.0.0.0:5000/"

r = requests.get(baseURL)

#print(r.text)
lcd.simplePrint(r.text, 1)
