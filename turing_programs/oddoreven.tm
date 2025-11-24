




next:
	right
	goto checker

final_verdict:
	left
	
	if 0 goto type_even
	if 1 goto type_odd
	if 2 goto type_even
	if 3 goto type_odd
	if 4 goto type_even
	if 5 goto type_odd
	if 6 goto type_even
	if 7 goto type_odd
	if 8 goto type_even
	if 9 goto type_odd

checker:
	if 1 goto next
	if 2 goto next
	if 3 goto next
	if 4 goto next
	if 5 goto next
	if 6 goto next
	if 7 goto next
	if 8 goto next
	if 9 goto next
	if 0 goto next
	
	if _ goto final_verdict
	
	goto type_invalid

start:
	if 0 goto type_even
	if _ goto type_invalid
	
	goto checker
	
type_invalid:
	right
	right
	write I
	right
	write N
	right
	write V
	right
	write A
	right
	write L
	right
	write I 
	right
	write D

type_even:
	right
	right
	write E
	right
	write V
	right
	write E
	right
	write N
	halt
	
type_odd:
	right
	right
	write O
	right
	write D
	right
	write D
	halt

