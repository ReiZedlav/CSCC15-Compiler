

ELSE:
	RIGHT
	
	GOTO START
	

START:
	IF 1 GOTO check_next
	IF 0 GOTO check_next
	IF _ GOTO write_one
	
	GOTO ELSE
	
check_next:
	RIGHT
	GOTO START

write_one:
	WRITE 1
	HALT

