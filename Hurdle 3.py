def turn_right():
    turn_left()
    turn_left()
    turn_left()

def forward():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while at_goal()==False:
    if wall_in_front():
       forward()
    else:
        move()
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
