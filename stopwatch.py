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
lapTimeNumber = 1
def timerStop():
    global  run
    run = False



def timerStart():
    global run, toggle, time_start
    run = True
    toggle +=1
    if toggle > 1:
        timerStop()
        startButton.config(text='Start')
        toggle=0
    time_start = time.time()
    refreshSwatch()
    startButton.config(text='Stop')


def clear():
    global run, toggle, totalTime, timerMS, timerSec, timerMIn
    run = False
    toggle = 0
    timerMS=0
    timerSec=0
    timerMin=0
    totalTime = str(timerMin) + ":" + str(timerSec).zfill(2) + ":" + str(timerMS).zfill(2) 
    timeStr.set(totalTime)
    lapOneStr.set("00:00:00")
    
def timeNow():
    now.set(datetime.datetime.now().strftime('%I:%M %p'))


def refresh():
    now.set(datetime.datetime.now().strftime('%I:%M %p'))
    currentTime.after(60000, refresh)


def refreshSwatch():
    global timerSec
    global timerMin
    global totalTime
    global timerMS
    if (run):
        time_now = time.time()
        stopwatch_time = time_now - time_start
        ms = int(round(stopwatch_time * 1000))
        timerMS = ms%1000
        timerSec = int((ms-timerMS)/1000)%60
        timerMin = int(int(ms-timerMS-(timerSec*1000))/60000)
        totalTime = str(timerMin) + ":" + str(timerSec).zfill(2) + ":" + str(timerMS).zfill(2)
        
        timeStr.set(totalTime)
        stopWatch.after(1, refreshSwatch)

def lapTime():
    global totalTime, lapTimeNumber
    if lapTimeNumber == 1:
        lapOneStr.set(totalTime)
                
frame = Tk()
frame.wm_title("Stopwatch")
now = StringVar()
timeStr = StringVar()
timeStr.set("00:00:00")
lapOneStr = StringVar()
lapTwoStr = StringVar()
lapOneStr.set('00:00:00')
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

lapOne = ttk.Label(frame, text='Lap 1: ')
lapOne.pack()
lapOneTime = ttk.Label(frame, textvariable=lapOneStr)
lapOneTime.pack()
lapOneButton = ttk.Button(frame, text='Lap', command=lapTime)
lapOneButton.config(pad=(90,5))
lapOneButton.pack()





startButton.pack()
stopButton.pack()
refresh()
frame.mainloop()
