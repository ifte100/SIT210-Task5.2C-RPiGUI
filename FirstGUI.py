from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

###hardware
ledRed = LED(14)
ledYellow = LED(16)
ledBlue = LED(25)


##GUI DEFINITIONs
win = Tk()
win.title("LED GUI")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
##EVENT FUNCTIONS
def RedledToggle():
    if ledRed.is_lit:
        ledRed.off()
        ledButtonRed["text"] = "Turn RED LED on"
    else:
        ledRed.on()
        ledButtonRed["text"] = "Turn RED LED off"
        
def YellowledToggle():
    if ledYellow.is_lit:
        ledYellow.off()
        ledButtonYellow["text"] = "Turn Yellow LED on"
    else:
        ledYellow.on()
        ledButtonYellow["text"] = "Turn Yellow LED off"
        
def BlueledToggle():
    if ledBlue.is_lit:
        ledBlue.off()
        ledButtonBlue["text"] = "Turn Blue LED on"
    else:
        ledBlue.on()
        ledButtonBlue["text"] = "Turn Blue LED off"
    
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        
###WIDGETS
ledButtonRed = Button(win, text = 'Turn Red LED On', font = myFont, command = RedledToggle, bg = 'Red', height = 1, width = 24)        
ledButtonRed.grid(row = 0, column = 1)

ledButtonYellow = Button(win, text = 'Turn Yellow LED On', font = myFont, command = YellowledToggle, bg = 'Yellow', height = 1, width = 24)        
ledButtonYellow.grid(row = 1, column = 1)

ledButtonBlue = Button(win, text = 'Turn Blue LED On', font = myFont, command = BlueledToggle, bg = 'Blue', height = 1, width = 24)        
ledButtonBlue.grid(row = 2, column = 1)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'white', height = 1, width = 3)
exitButton.grid(row = 3, column = 1)


win.protocol("WM_DELETE_WINDOW", close) ##exit using the exit icon
win.mainloop() #for looping forever