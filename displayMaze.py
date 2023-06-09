import turtle

def displayMaze(edgeList, r, c):
    win_width, win_height, bg_color = 2000, 2000, 'white'

    turtle.setup()
    turtle.screensize(win_width, win_height, bg_color)
    turtle.speed(0)
    turtle.pensize(1)
    turtle.color("gray")
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

    for row in range(r+1):
        if(row == 0 or row == r):
            turtle.pensize(3)
        else: 
            turtle.pensize(1)
        turtle.penup()
        turtle.goto(-850, 400 - row * 50)
        turtle.pendown()
        turtle.forward(c * 50)

    turtle.penup()

    for col in range(c+1):
        if col==0 or col==c:
            turtle.pensize(3)
        else:
            turtle.pensize(1)
        turtle.penup()
        turtle.goto(-850 + col * 50, 400)
        turtle.pendown()
        turtle.setheading(90)  
        turtle.forward(-r * 50)

    turtle.penup()

    turtle.pensize(6)
    turtle.color("blue")

    for cell in range(r * c):
        x = cell % c
        y = cell // c

        if {cell, cell + c} not in edgeList and cell+c < r*c:
            # print(cell,cell+c," y1")
            # turtle.color("blue")
            x1 = -850 + x * 50
            y1 = 350 - y * 50
            x2 = -850 + (x + 1) * 50
            y2 = 350 - y * 50

            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.goto(x2, y2)

        if {cell, cell + 1} not in edgeList and cell//c == (cell+1)//c : 
            # turtle.color("red")
            # print(cell,cell+1," x1")
            x1 = -800 + x * 50
            y1 = 400 - y * 50
            x2 = -800 + x * 50
            y2 = 400 - (y + 1) * 50

            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.goto(x2, y2)

    turtle.penup()
    turtle.hideturtle()
    turtle.done()
