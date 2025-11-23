

write_binary:
	write 1
	right
	write 1
	right
	write 0
	right
	write 1
	right
	write 0

start:
	if _ goto write_binary
	right
	goto start
