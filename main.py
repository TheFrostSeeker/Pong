# Imports
import turtle
import winsound

# Setting the environnement
window = turtle.Screen()  # Window's creation
window.title("Pong en python")  # Title's creation
window.bgcolor("black")  # Change background color
window.setup(width=800, height=600)  # Set the window scale
window.tracer(0)  # Stop window's update

# Score
score_a, score_b = 0, 0  # Set base scores

# Paddle A
paddle_a = turtle.Turtle()  # Creating 1st paddle
paddle_a.speed(0)  # Set animation's speed to 0
paddle_a.shape("square")  # Add a square shape
paddle_a.color("white")  # Add color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square by 5 time his width
paddle_a.penup()  # 'Up the pen' to not drawn on the screen with the shape
paddle_a.goto(-350, 0)  # Set the paddle location

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  # Movement speed to the right
ball.dy = 0.1  # Movement speed to the top

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  # Hide the drawing
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))  # Setting text


# Functions
def paddle_a_up():
    y = paddle_a.ycor()  # Return the y coordinate from the paddle
    y += 20  # Add 20pxl to the coordinate
    paddle_a.sety(y)  # Set the y paddle's position to the new y position


def paddle_a_down():
    y = paddle_a.ycor()  # Return the y coordinate from the paddle
    y -= 20  # Remove 20pxl to the coordinate
    paddle_a.sety(y)  # Set the y paddle's position to the new y position


def paddle_b_up():
    y = paddle_b.ycor()  # Return the y coordinate from the paddle
    y += 20  # Add 20pxl to the coordinate
    paddle_b.sety(y)  # Set the y paddle's position to the new y position


def paddle_b_down():
    y = paddle_b.ycor()  # Return the y coordinate from the paddle
    y -= 20  # Remove 20pxl to the coordinate
    paddle_b.sety(y)  # Set the y paddle's position to the new y position


# Keyboard binding
window.listen()  # Listen the keyboard input
window.onkeypress(paddle_a_up, "z")  # Set the paddle up function when press the key
window.onkeypress(paddle_a_down, "s")  # Set the paddle down function when press the key
window.onkeypress(paddle_b_up, "Up")  # Set the paddle up function when press the arrow key
window.onkeypress(paddle_b_down, "Down")  # Set the paddle down function when press the arrow key

####################
#  Main game loop  #
####################
while True:
    window.update()  # Get window open

    # Ball's movement
    ball.setx(ball.xcor() + ball.dx)  # Add ball.dx to the ball's coordinate
    ball.sety(ball.ycor() + ball.dy)  # Same for y

    # Border checking
    if ball.ycor() > 290:  # If the y ball's coordinate hit the top
        ball.sety(290)  # Set the coordinate to the max
        ball.dy *= -1  # And reverse the direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Add a sound on collision

    if ball.ycor() < -290:  # Same when hiting the bottom
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:  # If the ball go out of the screen
        ball.goto(0, 0)  # Go back to the center
        ball.dx *= -1  # Then, reverse direction
        score_a += 1  # Add 1 point to player A
        pen.clear()  # Clear old text
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))  # Update text

    if ball.xcor() > 390:  # Same for the other direction
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # Reverse direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
