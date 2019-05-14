WIDTH = 712
HEIGHT = 508

step = 1
frames = 0


def get_alien_image(setp):
    return "p1_walk%02d" % step


alien = Actor(get_alien_image(step), pos=(100, 100))


def update():
    global frames
    global step

    frames += 1

    if frames % 5 == 0:
        step = (step % 11) + 1
        alien.image = get_alien_image(step)


def draw():
    screen.fill((0, 0, 0))
    alien.draw()
