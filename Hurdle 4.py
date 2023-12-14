def turn_right():
    turn_left()
    turn_left()
    turn_left()

def forward():
   
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not(at_goal()):
    if wall_in_front():
       forward()
    else:
        move()
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
