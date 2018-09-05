import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

# Square
def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)
        

for i in range(100):
    square(100,90)
    my_turtle.left(13)
# Circle has 360 degrees
# 360/15 --> 24

