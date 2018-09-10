# Input: Lock on position
# output: Laser position



# "Ultra Square Root" (Now with more decimal places!)
def usqrt(n):
	# 100 decimal places of sqrt(2)
	longer_sqrt = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
	return (longer_sqrt * n)//(10**100)

# Calculate the answer
def calculate(n):
	# Skip calculation if the number is 1 or less than 1
	if n == 1:
		return 1
	elif n <= 0:
		return 0
	
	# Return a recursive equation
	return n*usqrt(n) + n*(n+1)/2 - usqrt(n)*(usqrt(n) +1)/2 - calculate(usqrt(n))


def answer(n):
	n = long(n)
	return str(calculate(n))

print answer("5")