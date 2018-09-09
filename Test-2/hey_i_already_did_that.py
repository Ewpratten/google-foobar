# Input: n, b
# Output: number of cycles
import string # Used to check if the input is incorrect

def convert_base(number, b):
	# Convert a base 10 number to base b
    if b < 2:
        return False
    remainders = []
    while number > 0:
        remainders.append(str(number % b))
        number //= b
    remainders.reverse()
    return ''.join(remainders)

def sortNumbers(input_string, reverse):
	# A wrapper for python's sort function
	input_string = list(input_string)
	input_string.sort(reverse=reverse)
	output = ""
	# Convert list back to string
	for number in input_string:
		output += str(number)
	return output

def paddedStr(z, k):
	output = ""
	z = str(z)
	# Make the string of legnth k by adding 0s to the start
	for _ in range(0, k - len(z)):
		output += "0"
	output += z
	return str(output)

def correctBase(n, b):
	# Convert to list
	numbers = list(n)
	# Check it it is a letter
	for number in numbers:
		if number in string.ascii_letters:
			return False
		# Make sure the input is the same base it is supposed to be
		if int(number) >= b:
			return False
	return True

def answer(n, b):
	# Initalize variables
	k = len(n)
	prev_values = {}
	
	# Check edge cases
	if k < 2 or k > 9:
		return 0
	
	if b < 2 or b > 10:
		return 0
	
	if not correctBase(n, b):
		return 0
	
	if int(n) < 0 or int(n) > 999999999:
		return 0
	
	# Main algorythmic loop
	position = 0
	while True:
		# Sort the numbers
		x = int(sortNumbers(n, True), b)
		y = int(sortNumbers(n, False), b)
		
		# create the next n
		z = x - y
		z = convert_base(z, b)
		n = paddedStr(z, k)	# Add leading zeros
		
		# If the current number has already been generated, this must be a loop
		if n in prev_values:
			# Return the distance from start to finish of the loop
			return position - prev_values[n]
		
		# Add the number to the list of seen numbers along with when it was generated
		prev_values[n] = position
		
		# Increment the position
		position += 1

# Used for testing
# print answer("210022", 3)