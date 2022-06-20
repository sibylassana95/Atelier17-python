# Utilisation d’un module : Turtle
# 1. Écrire un programme carre.py qui trace un carré.

from turtle import *

c=2
u=100
for k in range(4):
    forward(c*u)
    left(90)
exitonclick()
