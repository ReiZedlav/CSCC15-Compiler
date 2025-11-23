
write_word:
	write w
	right
	write o
	right
	write r
	right
	write d

start:
	if _ goto write_word
	right
	goto start
