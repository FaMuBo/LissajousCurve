import turtle
from math import cos, sin

pen = turtle.Turtle()
pen.hideturtle()
pen.speed("fastest")
pen.width(3)
pen.color("#AA00AA")

pen.up()
print("this program created by fatih mucahit bodur by using python programming language.")
print("enter your input and see your input's lissajous curve :)")
A1 = input ("Enter A number: ")
A = int(A1)

B1 = input ("Enter B number: ")
B = int(B1)

a1 = input ("Enter a number: ")
a = int(a1)

b1 = input ("Enter b number: ")
b = int(b1)

delta1 = input ("Enter delta  number: ")
delta = int(delta1)

t1 = input ("Enter t number: ")
t = int(t1)

for i in range(0, 1000):
  t += 0.01
  x = A * sin(a * t + delta)
  y = B * sin(b * t)
  pen.goto(x, y)
  pen.down()