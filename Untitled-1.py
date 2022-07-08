
from turtle import forward
from BirdBrain import Finch
import time

myFinch = Finch('A')

myFinch.setTurn('L', 60, 10)
myFinch.setMove('F', 10, 5)
myFinch.setTurn('R', 60, 10)
myFinch.setMove('F', 10, 5)
myFinch.setTurn('R', 60, 10)
myFinch.setMove('F', 10, 5)
myFinch.setTurn('R', 120, 10)
myFinch.setMove('F', 20, 10)