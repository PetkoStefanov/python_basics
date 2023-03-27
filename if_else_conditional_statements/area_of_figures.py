from math import pi

text = str(input())
s = float

if text == "square":
    a = float(input())
    s = a * a

elif text == "rectangle":
    a = float(input())
    b = float(input())
    s = a * b

elif text == "circle":
    r = float(input())
    s = pi * r ** 2

elif text == "triangle":
    a = float(input())
    h = float(input())
    s = (a * h) / 2

print("%.3f" % s)

