import turtle

t = turtle.Turtle()
t.penup()

s = turtle.Screen()
s.colormode(255)
s.setup(350, 350)
s.bgcolor(77,166,255)

def square(xloc, yloc, size, ccode1, ccode2, ccode3):
    t.setpos(xloc, yloc)
    t.pendown()
    t.fillcolor(ccode1, ccode2, ccode3)
    t.begin_fill()
    for i in range(1, 5):
        t.forward(size)
        t.right(90)
    t.end_fill()
    print("Made a square at: " + str(xloc) + "," + str(yloc) + " with size: " + str(size) + ".")
    t.penup()

def triangle(xloc, yloc, size, ccode1, ccode2, ccode3, direction = "left"):
    t.setpos(xloc, yloc)
    t.pendown()
    t.fillcolor(ccode1, ccode2, ccode3)
    t.begin_fill()
    for i in range(1, 4):
        t.forward(size)
        if direction is "left":
            t.left(120)
        else:
            t.right(130)
    t.end_fill()
    print("Made a triangle at: " + str(xloc) + "," + str(yloc) + " with size: " + str(size) + ".")
    t.penup()

def rectangle(xloc, yloc, size, size2, ccode1, ccode2, ccode3, direction = "right"):
    t.setpos(xloc, yloc)
    t.pendown()
    t.fillcolor(ccode1, ccode2, ccode3)
    t.begin_fill()
    for i in range(1, 5):
        if i % 2:
            t.forward(size2)
            if direction is "right":
                t.right(90)
            else:
                t.left(90)
        else:
            t.forward(size)
            if direction is "right":
                t.right(90)
            else:
                t.left(90)
    t.end_fill()
    print("Made a rectangle at: " + str(xloc) + "," + str(yloc) + " with size: " + str(size) + ".")
    t.penup()

def circle(xloc, yloc, size, ccode1, ccode2, ccode3):
    t.setpos(xloc, yloc)
    t.pendown()
    t.fillcolor(ccode1, ccode2, ccode3)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    print("Made a circle at: " + str(xloc) + "," + str(yloc) + " with size: " + str(size) + ".")
    t.penup()

#sun
circle(100, 80, 30, 253, 202, 0)
#house base
square(-75, 0, 150, 204, 122, 78)
#chimney
rectangle(60, 0, 40, 15, 0, 0, 0, "left")
#roof
triangle(-75, 0, 150, 179, 68, 0)
#door
rectangle(-15, -90, 60, 30, 242, 129, 48)
#doorknob
circle(10, -125, 3, 255, 221, 0)
#window 1
circle(0, 20, 30, 136, 153, 169)

t.setpos(0, 20)
t.pendown()
t.left(90)
t.forward(60)
t.penup()

t.setpos(-30, 50)
t.pendown()
t.right(90)
t.forward(60)
t.penup()

#window 2
circle(0, -70, 30, 136, 153, 169)

t.setpos(0, -70)
t.pendown()
t.left(90)
t.forward(60)
t.penup()

t.setpos(-30, -40)
t.pendown()
t.right(90)
t.forward(60)
t.penup()

#ending the drawing by hiding the turtle and closing on click
t.setpos(200, 200)
s.exitonclick()