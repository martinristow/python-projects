def turn_left():
    print("Turning left")

def at_goal():
    print("Goal")

def wall_in_front():
    print("Wall In Front")

def right_is_clear():
    print("Right is Clear")
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move():
    print("Moving...")

def front_is_clear():
    print("Front is Clear")

def path():
    while not at_goal():
        if wall_in_front() and not right_is_clear():
            turn_left()
        elif not wall_in_front() and right_is_clear():
            turn_right()
            move()
        elif wall_in_front():
            if right_is_clear():
                turn_right()
                move()
            else:
                turn_left()
        elif front_is_clear():
            move()

path()