
beginning:
	left
	if C goto stop
	write _ 
	goto beginning

end:
	if _ goto beginning
	right
	goto end

start:
	write C
	goto end

stop:
	write _
	halt