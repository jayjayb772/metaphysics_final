# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

#i = 0

#myStr = "TEST STRING"

#strLen = len(myStr)
def simplePrint(str,line):
    mylcd.lcd_display_string(str,line)


def clear():
    mylcd.lcd_clear()

degSymb = [0b01100,0b10010,0b10010,0b01100,0b00000,0b00000,0b00000,0b00000]





def simpleDelay(str,line,delay):
    i = 1
    mLen = len(str)
    while i<mLen+2:
        mylcd.lcd_display_string(str[0:i-1],line)
        i+=1
        sleep(delay*(i/mLen))



def multiLines(strs,start):
    for i in range(len(strs)):
        simplePrint(strs[i],start)
        start+=1


        



def testLCD():
    mone = ["hello", "my", "Friends"]
    mtwo = ["I am bored", "This is a test", "hi", "more lines"]
    longStr = "Hello my friends!!!!"
    simplePrint(longStr,2)
    sleep(1)
    simplePrint("clearing now",1)
    sleep(0.25)
    clear()
    simpleDelay(longStr,1,0.001)
    sleep(1)
    clear()
    multiLines(mone,1)
    sleep(1)
    clear()
    multiLines(mtwo,1)
    sleep(1)
    clear()
    simplePrint("Done",1)


