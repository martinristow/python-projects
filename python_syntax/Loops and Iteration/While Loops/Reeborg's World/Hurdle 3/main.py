def turn_left():
    print("Turning Left...")

def move():
    print("Moving...")

def at_goal():
    print("At Goal")


def wall_in_front():
    print("Wall In Front...")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def path():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        path()
    else:
        move()


