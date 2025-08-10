import turtle
turtle.Screen().bgcolor("maroon")
turtle.Screen().setup(300, 400)
board = turtle.Turtle()

for i in range(2):
    board.left(120)
    board.forward(100)

board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(60)

for i in range(3):
    board.forward(100)
    board.right(120)

board.forward(100)

turtle.done()



