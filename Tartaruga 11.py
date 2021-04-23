# -*- coding: utf-8 -*-

import turtle
a = turtle.Screen()
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Alterando o tamanho da caneta
tartaruga.pensize(6)
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(250)
    tartaruga.right(90)
a.exitonclick()