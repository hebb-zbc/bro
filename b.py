#!/usr/bin/env python3

import turtle
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(200,-200)
t.pendown()

for i in range(120):
  t.left(93)
  t.forward(500)

turtle.exitonclick()
