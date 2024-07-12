def turn_left():
    print("Turning left...")

def move():
    print("Moving...")

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

number = 6
while number > 0:
    path()
    number -= 1
