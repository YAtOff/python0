WIDTH = 712
HEIGHT = 508


alien = Actor("alien", pos=(0, 100))


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        print("you missed me!")


def set_alien_hurt():
    print("Eek!")
    sounds.eep.play()
    alien.image = "alien_hurt"
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = "alien"


def update():
    if keyboard.left:
        delta = -1
    elif keyboard.right:
        delta = 1
    else:
        delta = 0
    alien.right += delta


def draw():
    screen.fill((255, 0, 0))
    alien.draw()
