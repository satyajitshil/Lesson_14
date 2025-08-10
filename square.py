import turtle

turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(300,400)
t = turtle.Turtle()

for i in range(4):
    t.fd(100)
    t.rt(90)

turtle.done()