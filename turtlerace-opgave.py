import random
import turtle

# funktion til at tegne "banen"
# y er banens "højde" i skærmbiledet
# p er den turtle, som skal løbe på "banen"
def bane(p, y):
    p.penup()
    p.goto(400, y)
    p.right(90)
    p.pendown()
    p.circle(25)
    p.left(90)
    p.penup()
    p.goto(-400,y)
    p.pendown()


t = turtle.Turtle('turtle')
t.color('blue')

s = turtle.Turtle('turtle')
s.color('green')

# tegn banerne:
bane(noget)
bane(nogetandet)

while True:
    t.forward(random.randrange(0, 10))
    s.forward(random.randrange(0, 10))
    if(t.pos() >= (400, 0) or s.pos() >= (400, 0)): break

turtle.done()
