
write_n:
	write n
	halt

next:
	right
	right
	goto start

start:
	if n goto next
	if _ goto write_n
	
