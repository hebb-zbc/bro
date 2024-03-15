# Afslut figuren, så den slutter i samme punkt, som den starter 
# (og sæt farten lidt op?)

import turtle
t = turtle.Turtle()
t.speed(1)

# gå til begundelsespunktet
t.penup()
t.goto(200,-200)
t.pendown()

# tegn
for i in range(4):
  t.left(93)
  t.forward(500)

turtle.exitonclick()
