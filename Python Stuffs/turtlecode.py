#importing libraries
import turtle, random

myturtle = turtle.Turtle()
window = turtle.Screen()
#grid system
myturtle.goto(300,0)
myturtle.goto(-300,0)
myturtle.goto(0,0)
myturtle.goto(0,300)
myturtle.goto(0,-300)

myturtle.speed(100)
#circles


for i in range(100):
    #colors
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    turtle.colormode(255)
    #random coordinates
    circleX = random.randint(-290,-10)
    circleY = random.randint(10,290)
    #taking action
    myturtle.pencolor(red, green, blue)
    myturtle.penup()
    myturtle.goto(circleX,circleY)
    myturtle.pendown()
    myturtle.circle(10)


window.mainloop()