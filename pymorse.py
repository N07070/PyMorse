#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
What I need :

A function to get the user text and remove all what's not needed
    * Consider spaces
    * Consider é à è etc...
    * Consider punctuation
    * Consider Maj
    
1 for -
0 for .
    
A function to translate the text to morse code

A function to translate morse code to text

A function to output the morse code to GPIO 

A function to capture morse code from GPIO
"""

import RPi.GPIO as GPIO
import re,time, os

def get_user_text():
    user_text = raw_input("Please enter the message you would lile to broadcast. >> ")
    user_text = user_text.lower()
    word_list = list(user_text)
    return word_list


def long_pulse(pin):
    # os.system("ogg123 audio/long.ogg")
    GPIO.output(pin,GPIO.HIGH)
    print("-")
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW) 
	
def short_pulse(pin):
    # os.system("ogg123 audio/short.ogg")
    GPIO.output(pin,GPIO.HIGH)
    print(".")
    time.sleep(0.5)
    GPIO.output(pin,GPIO.LOW)
    


def text_to_morse_code(alpha_text):
    morse_code = []
    for letter in alpha_text:
        if letter == "a" or letter == "à" or letter == "â" or letter == "ä":
            morse_code.append("01")
        if letter == "b":
            morse_code.append("1000")
        if letter == "c":
            morse_code.append("1010")
        if letter == "d":
            morse_code.append("100")
        if letter == "e" or letter == "è" or letter == "é" or letter == "ê":
            morse_code.append("0")
        if letter == "f":
            morse_code.append("0010")
        if letter == "g":
            morse_code.append("110")
        if letter == "h":
            morse_code.append("0000")
        if letter == "i" or letter == "î" or letter == "ï":
            morse_code.append("00")
        if letter == "j":
            morse_code.append("0111")
        if letter == "k":
            morse_code.append("101")
        if letter == "l":
            morse_code.append("0100")
        if letter == "m":
            morse_code.append("11")
        if letter == "n":
            morse_code.append("10")
        if letter == "o":
            morse_code.append("111")
        if letter == "p":
            morse_code.append("0110")
        if letter == "q":
            morse_code.append("1101")
        if letter == "r":
            morse_code.append("010")
        if letter == "s":
            morse_code.append("111")
        if letter == "t":
            morse_code.append("0")
        if letter == "u":
            morse_code.append("001")
        if letter == "v":
            morse_code.append("0001")
        if letter == "w":
            morse_code.append("011")
        if letter == "x":
            morse_code.append("1001")
        if letter == "y":
            morse_code.append("1011")
        if letter == "z":
            morse_code.append("1100")
        if letter == ".":
            morse_code.append("010101")
        if letter == " ":
            morse_code.append(" ")
        else:
            pass
    morse_code = ''.join(map(str, morse_code))
    morse_code = list(morse_code)
    return morse_code

def broadcast_code(code_to_broadcast, pin):
    
    # Set the board as BOARD
    GPIO.setmode(GPIO.BOARD)
    print("Set the board to BOARD")
    
    # Setup the n th pin to OUTPUT
    GPIO.setup(pin, GPIO.OUT)
    print("Set the "+str(pin)+"th to OUTPUT")
    
    # Starting the broadcast
    print("Starting Broadcast")
    start_broadcast = [0,1,0,1]
    
    for x in start_broadcast:
        if x == 1:
            long_pulse(pin)
        if x == 0:
            short_pulse(pin)
    
    print("Broadcasting")
    for number in code_to_broadcast:
        if number == '1':
            long_pulse(pin)
        if number == '0':
            short_pulse(pin)
    
    #Boardcast end of transmission.
    print("Ending Boardcast")
    end_broadcast = [0,0,0,1,0,1]
    
    for y in end_broadcast:
        if y == 1:
            long_pulse(pin)
        if y == 0:
            short_pulse(pin)

    
    GPIO.cleanup()
    print("Cleaned up the board.")

def get_code_broadcast():
    #
    #GPIO.output(pin,True)
    print("Hello")

if __name__ == '__main__':

    code = get_user_text()
    code = text_to_morse_code(code)
    broadcast_code(code,7)
    
    
"""
# Todo
def morse_code_to_text(morse_code):
        morse_code = []
    for letter in morse_code:
        if letter == "01":
            morse_code.append("a")
        if letter == "1000":
            morse_code.append("b")
        if letter == "1010":
            morse_code.append("c")
        if letter == "100":
            morse_code.append("d")
        if letter == "e" or letter == "è" or letter == "é" or letter == "ê":
            morse_code.append("0")
        if letter == "f":
            morse_code.append("0010")
        if letter == "g":
            morse_code.append("110")
        if letter == "h":
            morse_code.append("0000")
        if letter == "i" or letter == "î" or letter == "ï":
            morse_code.append("00")
        if letter == "j":
            morse_code.append("0111")
        if letter == "k":
            morse_code.append("101")
        if letter == "l":
            morse_code.append("0100")
        if letter == "m":
            morse_code.append("11")
        if letter == "n":
            morse_code.append("10")
        if letter == "o":
            morse_code.append("111")
        if letter == "p":
            morse_code.append("0110")
        if letter == "q":
            morse_code.append("1101")
        if letter == "r":
            morse_code.append("010")
        if letter == "s":
            morse_code.append("111")
        if letter == "t":
            morse_code.append("0")
        if letter == "u":
            morse_code.append("001")
        if letter == "v":
            morse_code.append("0001")
        if letter == "w":
            morse_code.append("011")
        if letter == "x":
            morse_code.append("1001")
        if letter == "y":
            morse_code.append("1011")
        if letter == "z":
            morse_code.append("1100")
        if letter == ".":
            morse_code.append("010101")
        else:
            pass
    print(morse_code)
    print("Hello")"""
