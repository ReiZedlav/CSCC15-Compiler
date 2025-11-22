

check_next:
	right
	goto start

append_zero:
	write 1
	halt


start:
	if 1 goto check_next
	if 0 goto check_next
	if _ goto append_zero
