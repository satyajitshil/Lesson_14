import turtle

my_wn = turtle.Screen()
my_wn.bgcolor("blue")

my_wn.title("Turtle")
t = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        t.fd(size+1)
        t.lt(90)
        size = size - 5
    size = size + 1