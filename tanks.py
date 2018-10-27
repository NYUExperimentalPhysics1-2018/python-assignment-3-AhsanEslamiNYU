#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:18:02 2018

@author: gershow
"""
#done, Ahsan Eslami for Argha
import numpy as np
import matplotlib.pyplot as plt

tank1Color = 'b'
tank2Color = 'r'
obstacleColor = 'k'



def trajectory (x0,y0,v,theta,g = 9.8, npts = 100000):
    theta=np.deg2rad(theta)
    vx=v*np.cos(theta)
    vy=v*np.sin(theta)
    tf=vy/g+np.sqrt((vy/g)**2+2*(y0/g))
    t=np.linspace(0,tf,npts)
    
    xp= []
    yp= []
    for time in t:
        xp.append(x0+vx*time)
        yp.append(y0+vy*time-0.5*g*time**2)
        
    return xp, yp
 


def firstInBox (x,y,box):
    
#    for j in range(len(x)):
#        if box[1]<=x[j] and x[j]>=box[0]:
#            for jj in range (len(y)):
#                if y[jj]<=box[2] and y[jj]>=box[3]:
#                    return min(j,jj)
#        else:
#            return -1
    for j in range (len(x)):
        if x[j]>box[0] and x[j]<box[1] and y[j]>box[2] and y[j]<box[3]:
            return j
    return -1
        
    

def tankShot (targetBox, obstacleBox, x0, y0, v, theta, g = 9.8):
    
    x,y = trajectory(x0, y0, v, theta)
    x,y = endTrajectoryAtIntersection(x,y,obstacleBox)
    plt.plot(x,y,'k')
    plt.pause(0.001)
    plt.show()
    if firstInBox(x,y,targetBox) >= 0:
        return 1
    else:
        return 0

def drawBoard (tank1box, tank2box, obstacleBox, playerNum):
    plt.clf()
    drawBox(tank1box, tank1Color)
    drawBox(tank2box, tank2Color)
    drawBox(obstacleBox, obstacleColor)
    plt.xlim (0,100)
    plt.ylim(0,100)
    
    showWindow() #this makes the figure window show up

def oneTurn (tank1box, tank2box, obstacleBox, playerNum, g = 9.8):   
    plt.clf()
    drawBoard (tank1box, tank2box, obstacleBox, playerNum)

    v=getNumberInput ('what velocity')
    theta=getNumberInput ('what degree (if player2 enter between 90 and 180 degrees)')
    if playerNum==1:
        originBox=tank1box
        targetBox=tank2box
    else:
        originBox=tank2box
        targetBox=tank1box
    
    x0= (originBox[1]+originBox[0])/2
    y0=(originBox[3]+originBox[2])/2
    
    outcome=tankShot(targetBox, obstacleBox, x0, y0, v, theta, g=9.8)
    if outcome ==1:
        return playerNum
    else:
        return 0


    

def playGame(tank1box, tank2box, obstacleBox, g = 9.8):
    """
    parameters
    ----------
    tank1box : tuple
        (left,right,bottom,top) location of player1's tank
    tank2box : tuple
        (left,right,bottom,top) location of player1's tank
    obstacleBox : tuple
        (left,right,bottom,top) location of the central obstacle
    playerNum : int
        1 or 2 -- who's turn it is to shoot
     g : float 
        accel due to gravity (default 9.8)
    """
    outcome=0   
    playerNum=1
    while True:
        outcome=oneTurn (tank1box, tank2box, obstacleBox, playerNum, g=9.8)
        if outcome<0:
            break
        input ('hit enter to continue')
        playerNum=3-playerNum
    if outcome==1:
        print ('player 1 victory')
    else:
        print ('player 2 victory')
        
    
    
        
##### functions provided to you #####
def getNumberInput (prompt, validRange = [-np.Inf, np.Inf]):
    """displays prompt and converts user input to a number
    
       in case of non-numeric input, re-prompts user for numeric input
       
       Parameters
       ----------
           prompt : str
               prompt displayed to user
           validRange : list, optional
               two element list of form [min, max]
               value entered must be in range [min, max] inclusive
        Returns
        -------
            float
                number entered by user
    """
    while True:
        try:
            num = float(input(prompt))
        except Exception:
            print ("Please enter a number")
        else:
            if (num >= validRange[0] and num <= validRange[1]):
                return num
            else:
                print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") #Python 3 sytanx
            
    return num    

def showWindow():
    """
    shows the window -- call at end of drawBoard and tankShot
    """
    plt.draw()
    plt.pause(0.001)
    plt.show()


def drawBox(box, color):
    """
    draws a filled box in the current axis
    parameters
    ----------
    box : tuple
        (left,right,bottom,top) - extents of the box
    color : str
        color to fill the box with, e.g. 'b'
    """    
    x = (box[0], box[0], box[1], box[1])
    y = (box[2], box[3], box[3], box[2])
    ax = plt.gca()
    ax.fill(x,y, c = color)

def endTrajectoryAtIntersection (x,y,box):
    """
    portion of trajectory prior to first intersection with box
    
    paramaters
    ----------
    x,y : np array type
        position to check
    box : tuple
        (left,right,bottom,top)
    
    returns
    ----------
    (x,y) : tuple of np.array of floats
        equal to inputs if (x,y) does not intersect box
        otherwise returns the initial portion of the trajectory
        up until the point of intersection with the box
    """
    i = firstInBox(x,y,box)
    if (i < 0):
        return (x,y)
    return (x[0:i],y[0:i])


##### fmain -- edit box locations for new games #####
def main():    
    tank1box = [10,15,0,5]
    tank2box = [90,95,0,5]
    obstacleBox = [40,60,0,50]
    
    playGame(tank1box, tank2box, obstacleBox)
    

#don't edit the lines below;
if __name__== "__main__":
    main()  
        
    