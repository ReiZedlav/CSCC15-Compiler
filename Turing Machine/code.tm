
check_next:
	right
	goto start

remove_last:
	left
	write _
	halt

start:
	if 1 goto check_next
	if 0 goto check_next
	if _ goto remove_last
