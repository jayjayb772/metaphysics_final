import EasyLCD as lcd
import requests
import secrets
# from gpiozero import *
from time import *

access_token = secrets.access_token
authHeader = "Bearer " + access_token

mylcd = lcd.mylcd
running = True

global curLightMode
curLightMode = 2
global curTemp
curTemp = 0
global curGoalTemp
curGoalTemp = 0
global curFanState
curFanState = False
global curHeaterState
curHeaterState = False
global bsNumLightModes
bsNumLightModes = False

global coldButton
coldButton = Button(17)
global coldButtonPressed
coldButtonPressed = False

global hotButton
hotButton = Button(18)
global hotButtonPressed
hotButtonPressed = False

global lightButton
lightButton = Button(27)
global lightButtonPressed
lightButtonPressed = False

global fanOut
fanOut = LED(23)

global heaterOut
heaterOut = LED(22)


def makeGetRequest(command):
    response = requests.get(
        'https://api.particle.io/v1/devices/36003b001051363036373538/' + command + '?access_token=' + access_token)
    return response.json()['result']


def makePostRequest(command, arg):
    response = requests.post(
        'https://api.particle.io/v1/devices/36003b001051363036373538/' + command + '?access_token=' + access_token,
        data={'args': arg})
    return response.json()


def setFanState(state):
    if state == 1:
        fanOut.off()
    else:
        fanOut.on()


def setHeaterState(state):
    if state == 1:
        heaterOut.off()
    else:
        heaterOut.on()


def changeGoalTemp(val):
    newGoal = curGoalTemp + val
    return makePostRequest('SetGoalTemp', newGoal)


def changeLightMode():
    global curLightMode
    if curLightMode < bsNumLightModes - 1:
        newMode = curLightMode + 1
    else:
        newMode = 1
    curLightMode = newMode
    return makePostRequest('SetLightMode', newMode)


def updateAllVals():
    mylcd.clear()
    mylcd.simplePrint('Please Wait', 1)
    mylcd.simplePrint('Updating Values', 2)
    global curLightMode
    curLightMode = makeGetRequest('Light-Mode')
    # Get All Vals
    global curTemp
    curTemp = makeGetRequest('Temperature')
    # print(curTemp)
    global curGoalTemp
    curGoalTemp = makeGetRequest('Goal-Temperature')
    # print(curGoalTemp)
    # print(curLightMode)
    global curFanState
    curFanState = makeGetRequest('Fan-State')
    # print(curFanState)
    global curHeaterState
    curHeaterState = makeGetRequest('Heater-State')
    # print(curHeaterState)
    global bsNumLightModes
    bsNumLightModes = makeGetRequest('bsNumLightModes')


lightModes = ['Temperature', 'Rainbow', 'Clock', 'Rotate', 'Double Rotate']


def writeToScreen():
    mylcd.clear()
    lineZero = 'Temperature: ' + curTemp + 'F'
    lineOne = 'Goal Temp: ' + curGoalTemp + 'F'
    lineTwo = 'Light Mode:' + lightModes[curLightMode]
    mylcd.simplePrint(lineZero, 0)
    mylcd.simplePrint(lineOne, 1)
    mylcd.simplePrint(lineTwo, 2)


def checkButtonPresses():
    global lightButtonPressed
    global coldButtonPressed
    global hotButtonPressed

    if lightButton.is_pressed and lightButtonPressed == False:
        lightButtonPressed = True
        changeLightMode()

    if coldButton.is_pressed and coldButtonPressed == False:
        coldButtonPressed = True
        changeGoalTemp(-1)
    elif hotButton.is_pressed and hotButtonPressed == False:
        hotButtonPressed = True
        changeGoalTemp(1)
    if (lightButtonPressed and coldButtonPressed) or (lightButtonPressed and hotButtonPressed) or (
            coldButtonPressed and hotButtonPressed):
        mylcd.clear()
        mylcd.simplePrint('Slow Down Please', 1)
        sleep(2)
        writeToScreen()
    sleep(0.1)
    lightButtonPressed = False
    hotButtonPressed = False
    coldButtonPressed = False


while running:
    updateAllVals()
    # TODO: check if fan should be on
    if curFanState:
        setFanState(1)
    else:
        setFanState(0)
    if curHeaterState:
        setHeaterState(1)
    else:
        setHeaterState(0)

    writeToScreen()
    # TODO: Check for button presses
    for i in range(60):
        checkButtonPresses();

