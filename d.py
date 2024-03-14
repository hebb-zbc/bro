import turtle
t = turtle.Turtle()

def minlinje(x1, y1, x2, y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)


for i in range(0,11):
    x1 = 0
    y1 = (10-i) * 20
    x2 = i * 20
    y2 = 0
    minlinje(x1, y1, x2, y2)
    minlinje(-x1, -y1, -x2, -y2)
