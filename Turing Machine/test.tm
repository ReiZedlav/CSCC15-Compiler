
add_A:
	write A
	halt

start:
	if _ goto add_A
	right
	goto start