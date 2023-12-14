def turn_right():
    turn_left()
    turn_left()
    turn_left()

def forward():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while(not(at_goal())):
   forward()
    
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
