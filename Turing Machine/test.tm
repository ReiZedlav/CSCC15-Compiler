

write 1
right
write 0
right
write 1
right
write 0

write_one:
	write 1
	halt

start:
	if _ goto write_one
	right
	goto start
