




write_one:
	write 1
	halt

start:
	if _ goto write_one
	right
	goto start
