import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 

###hardware
ledRed = LED(14)

CODE =  {'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'}
        

def dot():
            ledRed.on()
            time.sleep(1)
            ledRed.off()
            time.sleep(0.5)

def dash():
            ledRed.on()
            time.sleep(2)
            ledRed.off()
            time.sleep(0.5)

def finalName(name):

	for letter in name.get():
			for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dash()
				elif symbol == '.':
					dot()
				else:
                                    time.sleep(0.5)

window = tk.Tk()
 
window.title("Blinking Morse Code")
 
name = tk.StringVar()


def clickMe():
    label.configure(text= 'Morse code of ' + name.get() + ' is working now')
    finalName(name)
    
def limitSize(*args):
    value = name.get()
    if len(value) > 12: name.set(value[:12])

def close():
    GPIO.cleanup()
    window.destroy()


label = ttk.Label(window, text = "Enter a word maximum 12 characters:")
label.grid(column = 0, row = 0)
 
    
name.trace('w', limitSize)##limiting the size of character input to 12

nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)

###buttons
button = ttk.Button(window, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)

exitButton = Button(window, text = 'EXIT', command = close, height = 1, width = 3)
exitButton.grid(column = 0, row = 3)


window.mainloop()
window.protocol("WM_DELETE_WINDOW", close) 