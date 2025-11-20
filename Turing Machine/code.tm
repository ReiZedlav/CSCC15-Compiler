WRITE 1
RIGHT
WRITE 0
RIGHT
WRITE 1

check_next:
    RIGHT
    GOTO START

WRITE_ONE:
    WRITE 1
    HALT

START:
    IF 1 GOTO check_next
    IF 0 GOTO check_next
    IF _ GOTO WRITE_ONE

    
