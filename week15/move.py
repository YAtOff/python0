import turtle
import math
import time


PLAYGROUND_WIDTH= 200
PLAYGROUND_HEIGHT= 200


def drow_border():
    mypen = turtle.Turtle()
    mypen.color('white')
    mypen.penup()
    mypen.setposition(-PLAYGROUND_WIDTH / 2, -PLAYGROUND_HEIGHT / 2)
    mypen.pendown()
    mypen.pensize(3)
    for side in [PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT,
                 PLAYGROUND_WIDTH, PLAYGROUND_WIDTH]:
        mypen.forward(side)
        mypen.left(90)
        mypen.hideturtle()


def create_player():
    player = turtle.Turtle()
    player.color('blue')
    player.penup()
    player.speed(0)
    return player


# Set up screen
window = turtle.Screen()
window.bgcolor('black')
window.tracer(0)

play_game = True

drow_border()

player = create_player()


def go_forward():
    # write code
    pass


def go_backward():
    # write code
    pass


def turn_rigth():
    # write code
    pass


def turn_left():
    # write code
    pass


def quit_game():
    global play_game
    play_game = False

# Set keyboard bindings
window.listen()
window.onkey(turn_left, 'Left')
window.onkey(turn_rigth, 'Right')
window.onkey(go_forward, 'Up')
window.onkey(go_backward, 'Down')
window.onkey(quit_game, 'q')

while play_game:
    start_time = time.clock()
    window.update()
    time.sleep(start_time + 0.01 - time.clock())

window.bye()
