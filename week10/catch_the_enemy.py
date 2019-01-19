import turtle
from random import randint


RIGHT = 0
DOWN = 270
LEFT = 180
UP = 90
PLAYER_STEP = 5  # пиксела на придвижване
ENEMY_STEP = 10  # пиксела на придвижване
ENEMY_SPEED = 200  # едно движение на 0.2 sec

screen = turtle.Screen()


def create_player():
    player = turtle.Turtle()
    player.shape('turtle')
    player.penup()
    player.fillcolor('blue')
    player.speed(0)  # това означава без анимация (най-бързото движение)
    return player


def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape('turtle')
    enemy.penup()
    enemy.fillcolor('red')
    enemy.speed(0)  # това означава без анимация (най-бързото движение)
    enemy.right(90)  # гледа надолу
    return enemy


def draw_border():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.hideturtle()
    for _ in range(4):
        t.forward(300)
        t.right(90)


player = create_player()
enemy = create_enemy()


def reset_enemy():
    enemy.goto(randint(-130, 130), 130)


def move_enemy():
    enemy.forward(ENEMY_STEP)

    # напишете кода
    # Ако врага и извън игралното поле - рестартирайте позицията му с `reset_enemy`
    # Ако врага е ударен - отбележете точка и рестартирайте позицията му
    # Използваъте `player.distance(enemy.pos())` - то ви дава диатанцията между играчите

    screen.ontimer(move_enemy, ENEMY_SPEED)


# Тези функции се викат при натискане на бутон
# Те трябва да придвижат играча в дадената посока
# за да завивате вземете текущата посока на играча (ъгъл) с `player.heading()`
# и пресметнете новате посока


def move_right():
    # напишете кода
    pass


def move_down():
    # напишете кода
    pass


def move_left():
    # напишете кода
    pass


def move_up():
    # напишете кода
    pass


draw_border()
reset_enemy()

# Движение:
#
#    W
#   A D
#    S
screen.onkey(move_up, 'e')
screen.onkey(move_down, 'd')
screen.onkey(move_left, 's')
screen.onkey(move_right, 'f')
screen.ontimer(move_enemy, ENEMY_SPEED)

screen.listen()
screen.mainloop()
