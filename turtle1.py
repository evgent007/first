import turtle
turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('green','red')

for s in range(20):
    turtle.color('green','red')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(360/3)
        turtle.color('red','blue') 
    turtle.end_fill()

    turtle.forward(50)
    turtle.right(60)

turtle.hideturtle()
