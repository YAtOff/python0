WIDTH = 960
HEIGHT = 600

STRIDE = 24
PLAYGROUND_WIDTH = WIDTH / STRIDE
PLAYGROUND_HEIGHT = HEIGHT / STRIDE

game = {
    "frames": 0,
    "status": "alive"
}
snake = {
    "head": (7, 1),
    "body": [
        (6, 1),
        (5, 1),
        (4, 1),
        (3, 1),
        (2, 1),
        (1, 1)
    ],
    "direction": "right",
    "speed": 10  # one move on 10 frames
}
fruit = {
    "position": (10, 5)
}
bomb = {
    "position": (5, 7)
}

def draw_image(image, position):
    screen.blit(
        image,
        (position[0] * STRIDE, position[1] * STRIDE)
    )

def draw_snake():
    head_image = "snake_head_{}".format(snake["direction"])
    draw_image(head_image, snake["head"])
    for part in snake["body"]:
        draw_image("snake_body", part)


def move_snake():
    head = snake["head"]
    body = snake["body"]
    direction = snake["direction"]

    dx = 0
    dy = 0
    if direction == "left":
        dx = -1
    elif direction == "up":
        dy = -1
    elif direction == "right":
        dx = 1
    elif direction == "down":
        dy = 1

    new_head = (head[0] + dx, head[1] + dy)

    snake["head"] = new_head
    body.pop()
    body.insert(0, head)


def set_snake_direction():
    if keyboard.left:
        snake["direction"] = "left"
    elif keyboard.up:
        snake["direction"] = "up"
    elif keyboard.right:
        snake["direction"] = "right"
    elif keyboard.down:
        snake["direction"] = "down"


def update():
    game["frames"] += 1

    if game["status"] != "alive":
        return

    set_snake_direction()
    if game["frames"] % snake["speed"] == 0:
        move_snake()


def draw():
    screen.clear()
    if game["status"] == "alive":
        draw_snake()
        draw_image("fruit", fruit["position"])
        draw_image("bomb", bomb["position"])
    else:
        screen.draw.text("Game over!", (WIDTH // 2, HEIGHT // 2))











