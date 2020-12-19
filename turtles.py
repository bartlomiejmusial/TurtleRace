from turtle import Turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


# Function to set turtles with different colors, in line
def set_turtles():
    turtle_red = Turtle(shape="turtle")
    turtle_red.penup()
    turtle_red.color(colors[0])
    turtle_red.goto(x=-230, y=-100)
    turtles.append(turtle_red)

    turtle_orange = Turtle(shape="turtle")
    turtle_orange.penup()
    turtle_orange.color(colors[1])
    turtle_orange.goto(x=-230, y=-60)
    turtles.append(turtle_orange)

    turtle_yellow = Turtle(shape="turtle")
    turtle_yellow.penup()
    turtle_yellow.color(colors[2])
    turtle_yellow.goto(x=-230, y=-20)
    turtles.append(turtle_yellow)

    turtle_green = Turtle(shape="turtle")
    turtle_green.penup()
    turtle_green.color(colors[3])
    turtle_green.goto(x=-230, y=20)
    turtles.append(turtle_green)

    turtle_blue = Turtle(shape="turtle")
    turtle_blue.penup()
    turtle_blue.color(colors[4])
    turtle_blue.goto(x=-230, y=60)
    turtles.append(turtle_blue)

    turtle_purple = Turtle(shape="turtle")
    turtle_purple.penup()
    turtle_purple.color(colors[5])
    turtle_purple.goto(x=-230, y=100)
    turtles.append(turtle_purple)

    return turtles
