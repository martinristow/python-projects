def turn_left():
    print("Turning Left...")

def move():
    print("Moving...")

def at_goal():
    print("At Goal")
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def path():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# while at_goal() != True:
#     path()

while not at_goal(): # better way for me
    path()

