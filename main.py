from turtle import Turtle, Screen
from turtles import set_turtles
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

# Pop-up to enter a bet
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter one of the colors of the rainbow: :")
turtles = set_turtles()

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
