# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:05:10 2017

@author: karen
"""
#python Desktop/MITRE_AMPL/MatplotGUI.py

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

#set values
TotalDistricts = 399 #max for district slider bar
TotalAppeals = 40   #max for appeals slider bar
MaxDistance = 500 #max distance between settlements and district courts in km
d0 = 200 #initial district court number value
a0 = 30  #initial appeals court number value
dist0 = 200 #initial max distance value


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.251)

#that sine wave plot
t = np.arange(0.0, 1.0, 0.001)
s = a0*np.sin(5*np.pi*d0*t)
l, = plt.plot(t, s, lw=2, color='blue')
plt.axis([0, 1, -10, 10])

#slider bars
axcolor = 'lightgrey'
slideD_axes = plt.axes   ([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
slideA_axes = plt.axes   ([0.25, 0.1,  0.65, 0.03], facecolor=axcolor)
slideDist_axes = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

slideD = Slider(slideD_axes, 'District Courts', 0, TotalDistricts, valinit=d0,valfmt='%0.0f')
slideA = Slider(slideA_axes, 'Appeals Courts', 0, TotalAppeals, valinit=a0,valfmt='%0.0f')
slideDist = Slider(slideDist_axes, 'Max Distance (km)', 0, MaxDistance, valinit=dist0,valfmt='%0.0f')

def update(val):
    maxOpenD = slideD.val
    maxOpenA = slideA.val
    maxDist = slideDist.val
    #remove this and replace with visualization
    l.set_ydata(maxOpenA*np.sin(2*np.pi*maxOpenD*t))
    fig.canvas.draw_idle()

slideD.on_changed(update)
slideA.on_changed(update)

def RunModel(val):
    maxOpenD = slideD.val
    maxOpenA = slideA.val
    maxDist = slideDist.val
    #make this call function to run gurobi/optimization model
    print('RUN!')


#buttons    
reset_axes = plt.axes([0.8,  0.01, 0.1, 0.04])
run_axes = plt.axes(  [0.65, 0.01, 0.1, 0.04])

resetButton = Button(reset_axes, 'Reset', color=axcolor, hovercolor='0.975')
runButton   = Button(run_axes, 'Run', color='skyblue' , hovercolor='lightblue' )

runButton.on_clicked(RunModel)

def reset(event):
    slideD.reset()
    slideA.reset()
    slideDist.reset()
resetButton.on_clicked(reset)

#radio buttons
raxes = plt.axes([0.01, .25, 0.1, 0.2], facecolor=axcolor)
radio = RadioButtons(raxes, ('red','blue'), active=0)

def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()

radio.on_clicked(colorfunc)



plt.show()
