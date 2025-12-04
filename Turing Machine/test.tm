if 1 goto mark_x
if 0 goto mark_y

mark_x:
	write x
	goto start

mark_y:
	write y
	goto start

start:
	if _ goto leastsignificantbit
	right
	goto start

leastsignificantbit:
	left

increment_bit:
	if 0 goto incrementlsb
	if 1 goto longaddition
	if y goto write_one

xor_carry:
	if x goto write_one_msb

	write 0
	left
	goto longaddition

longaddition:
	if 1 goto xor_carry
	if x goto write_one_msb
	if y goto write_one
	
incrementlsb:
	write 1
	goto msb

msb:
	if x goto write_one
	if y goto write_zero
	left
	goto msb



write_one_msb:
	write 1
	goto appendzerolsb

add_zero:
	write 0
	halt

appendzerolsb:
	if _ goto add_zero
	right
	goto appendzerolsb

write_one:
	write 1
	halt

write_zero:
	write 0
	halt
	

