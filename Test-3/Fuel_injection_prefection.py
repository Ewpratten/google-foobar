# Input: Number of pellets
# Output: Number of operations required to get just one pellet

def answer(n):
	# Convert to a number
	n = long(n)
	
	# Check edge cases
	if n <= 0: # Make sure there is not a negitivs number of pellets
		return 0
	if n > (1 * (10**309)) - 1: # Make sure there aren't more pellets than the display limit
		return 0
	
	# Dict to store return values for 1 and 2 pellets (replaces messy if-else statements)
	known_return_values = { long(1):0, long(2):1 }
	
	# Use recursion to help optomize code
	# Nested functions used to remove the need for global variables
	def find_steps(n):
		# Check if the answer for n is already known
		if n in known_return_values:
			return known_return_values[n]
		
		# Make sure a quantum antimatter pellet does not get cut in half
		if not n % 2 == 0:
			# Odd numbers require an extra operation due to the fact that they can not be divided
			operations = 2 # For readibility
			# Recursivly check the number using a bitwize shift untill only 1 pellet is left. Store the number of operations in a variable
			result = min(find_steps((n+1) >> 1) + operations,
						find_steps( (n-1) >> 1) + operations)
			# Add the number of operations required to the known values
			known_return_values[n] = result
		
		else:
			# Even numbers can be divided, only one operation is used
			operations = 1 # For readibility
			known_return_values[n] = find_steps( n >> 1) + operations
		
		# Return the number of operations required for n
		return known_return_values[n]
	
	# Recursive return
	return find_steps(n)

# print answer(4)