import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Background color

# Create a turtle named "artist"
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed

# Define a function to draw a colorful spiral
def colorful_spiral(size):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    for i in range(size):
        artist.pencolor(colors[i % len(colors)])  # Change color
        artist.forward(i * 10)  # Move forward
        artist.right(144)  # Turn right by 144 degrees

# Draw the spiral
colorful_spiral(100)

# Finish up
artist.hideturtle()  # Hide the turtle after drawing
turtle.done()  # Keep the window open
