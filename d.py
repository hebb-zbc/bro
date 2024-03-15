import turtle
t = turtle.Turtle()

# funktion til at tegne linje mellem 2 punkter
# punkt 1: x1 og y1
# punkt 2: x2 og y2
def minlinje(x1, y1, x2, y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

# tegn:
for i in range(0,11):
    # lav x og y-koordinater
    x1 = 0
    y1 = (10-i) * 20
    x2 = i * 20
    y2 = 0
    # tegn 2 linjer
    minlinje(x1, y1, x2, y2)
    minlinje(-x1, -y1, -x2, -y2)
