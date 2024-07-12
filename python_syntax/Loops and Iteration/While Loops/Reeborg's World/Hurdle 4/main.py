def turn_left():
    print("Turning Left...")

def move():
    print("Moving...")

def at_goal():
    print("At Goal")

def wall_in_front():
    print("Wall In Front")

def wall_on_right():
    print("Wall On Right")
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def path():
    while not at_goal():
        if wall_in_front():
            turn_left()
        else:
            move()
        if not wall_on_right():
            turn_right()


path()

