import turtle 
import time

width = 600
height = 500
S = turtle.Screen()
S.setup(width, height)
S.bgcolor("lightblue")
S.title("NEW YEAR COUNTDOWN")

countdown = 10

pen = turtle.Pen()
pen.hideturtle()

for timer in range(countdown, -1, -1):
    pen.clear()
    pen.write(timer, align = "center", font = (None, 80))
    time.sleep(1)

pen.clear()
pen.color("red")
pen.write("WISHING YOU A HAPPY NEW YEAR!", align="center", font = (None,25))    
time.sleep(2)