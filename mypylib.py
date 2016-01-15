def is_divisible(DIVIDEND, DIVISOR):
	# Is DIVIDEND divisible by DIVISOR?  Divide DIVIDEND by DIVISOR.  If the remainder is 0, return True.  Else, return False.
	# "%" is the modulo operator, it's like division, only it returns the remainder, not the quotient.
	if DIVIDEND % DIVISOR == 0:
		return True
	else:
		return False

def is_divisible_by_both(DIVIDEND, DIVISOR1, DIVISOR2):
	# Is DIVIDEND divisible by both DIVISOR1 and DIVISOR2?
	if ((is_divisible(DIVIDEND, DIVISOR1) == True) and (is_divisible(DIVIDEND, DIVISOR2) == True)):
		return True
	else:
		return False
