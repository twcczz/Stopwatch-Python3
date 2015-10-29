__author__ = 'Brian'
from tkinter import *
from tkinter import ttk
import datetime
import time
timerMS = 0
timerSec = 0
timerMin = 0
run = None
def timerStop():
    global  run
    run = False



def timerStart():
    global run
    run = True
    refreshSwatch()


def timeNow():
    now.set(datetime.datetime.now().strftime('%I:%M %p'))


frame = Tk()
frame.wm_title("Stopwatch")
now = StringVar()
timeStr = StringVar()
timeStr.set('0 min 0 sec 0 ms')
currentTime = ttk.Label(frame, textvariable=now)
currentTime.pack()
currentTime.config(font=('Courier', 45, 'bold'), pad=20)

stopWatch = ttk.Label(frame, textvariable=timeStr)
stopWatch.pack()


stopwatchLabel = ttk.Label(frame, text='Stopwatch')
stopwatchLabel.config(pad=(95, 5))

startButton = ttk.Button(frame, text='Start ', command=timerStart)
startButton.config(pad=(90, 5))

stopButton = ttk.Button(frame, text='Stop', command=timerStop)
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
        timerMS +=1
        if timerMS == 99:
            timerSec += 1
            timerMS = 0
            if timerSec == 59:
                timerMin += 1
                timerSec = 0
        totalTime = str(timerMin) + " min " + str(timerSec) + " sec " + str(timerMS) + " ms"
        timeStr.set(totalTime)
        stopWatch.after(10, refreshSwatch)


stopwatchLabel.pack()

startButton.pack()
stopButton.pack()
refresh()
frame.mainloop()
