__author__ = 'Brian'
from tkinter import *
from tkinter import ttk
import datetime
import time
timerMS = 0
timerSec = 0
timerMin = 0
run = None
toggle = 0
def timerStop():
    global  run
    run = False



def timerStart():
    global run, toggle
    run = True
    refreshSwatch()
    startButton.config(text='Stop')
    toggle +=1
    if toggle > 1:
        timerStop()
        startButton.config(text='Start')
        toggle=0

def clear():
    global run, toggle, totalTime, timerMS, timerSec, timerMIn
    run = False
    toggle = 0
    timerMS=0
    timerSec=0
    timerMin=0
    totalTime = str(timerMin) + " min " + str(timerSec) + " sec " + str(timerMS) + " ms"
    timeStr.set(totalTime)
    
def timeNow():
    now.set(datetime.datetime.now().strftime('%I:%M %p'))


frame = Tk()
frame.wm_title("Stopwatch")
now = StringVar()
timeStr = StringVar()
timeStr.set('0 min 0 sec 0 ms')
currentTime = ttk.Label(frame, textvariable=now)
currentTime.pack()
currentTime.config(font=('Courier', 25, 'bold'), pad=20, width=35, anchor=CENTER) #fixed some window bug, when the timeStr was longer than the width of windows

stopwatchLabel = ttk.Label(frame, text='Stopwatch')
stopwatchLabel.config(pad=(95, 5))
stopwatchLabel.pack()

stopWatch = ttk.Label(frame, textvariable=timeStr)
stopWatch.config(font=('Courier', 45, 'bold'), pad=20) # Here made the font bigger
stopWatch.pack()

startButton = ttk.Button(frame, text='Start ', command=timerStart)
startButton.config(pad=(90, 5))

stopButton = ttk.Button(frame, text='clear', command=clear)
stopButton.config(pad=(90, 5))


def refresh():
    now.set(datetime.datetime.now().strftime('%I:%M %p'))
    print('running')
    currentTime.after(60000, refresh)


def refreshSwatch():
    global timerSec
    global timerMin
    global totalTime
    global timerMS
    if run == True:
        timerMS += 1
        if timerMS == 99:
            timerSec += 1
            timerMS = 0
            if timerSec == 59:
                timerMin += 1
                timerSec = 0
        stopWatch.after(1, refreshSwatch)
        totalTime = str(timerMin) + " min " + str(timerSec) + " sec " + str(timerMS) + " ms"
        timeStr.set(totalTime)
        




startButton.pack()
stopButton.pack()
refresh()
frame.mainloop()
