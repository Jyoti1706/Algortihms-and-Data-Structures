import turtle
import trace
import sys

INCREMENT = 10
MAX_LENGTH = 340


def drawspiral(a_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    drawspiral(a_turtle, line_length + INCREMENT)


# charlie = turtle.Turtle(shape="turtle")
# charlie.pensize(5)
# charlie.color("red")
# charlie.speed(10)
# #drawspiral(charlie,10)
# turtle.done()

sys.path.append("..")

def factorial(n):
    # base case
    if n <= 1:
        return 1

    # move towards base case
    return n * factorial(n - 1)


n = 5

print(factorial(5))
