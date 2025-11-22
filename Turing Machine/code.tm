


write_zero:
	write 1
	right
	goto start

write_one:
	write 0
	right
	goto start

stop:
	left
	halt

start:
	if 0 goto write_zero
	if 1 goto write_one
	if _ goto stop
