
from turtle import forward
from BirdBrain import Finch
import time

myFinch = Finch('A')

while not myFinch.getButton('A'):
    if (myFinch.getLine('R') > 80 & myFinch.getLine('L') > 80):
        myFinch.setMotors(15,15)
    if (myFinch.getLine('R') < 80):
        myFinch.setMotors(20,0)
    if(myFinch.getLine('L') < 80):
        myFinch.setMotors(0,20)
    time.sleep(0.2)
myFinch.stop()

