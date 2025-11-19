
LEFT 
RIGHT
RIGHT
WRITE 1

check_left:
	LEFT
	
check_right:
    RIGHT
    LEFT

test:
    RIGHT
    LEFT
    HALT

start:
    LEFT
    RIGHT 
    LEFT
    WRITE 5
    GOTO check_left
    GOTO check_right
    IF 5 GOTO test
    

