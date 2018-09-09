# Input: List of the number of banannas owned by various guards
# Output: Number of guards that will be left watching the cells


# Custom implementation of fractions.gcd to reduce execution time by 0.2s
def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)

# Check if two numbers will produce an infinite loop
def infiniteLoop(x, y):
	z = (x + y) / gcd(x, y)
	return bool((z - 1) & z)

def match(bananna_counts):
	output = 0
	# Parse through all guards
	for i in range(3):
		for guard_1 in range(len(bananna_counts)/2):
			for guard_2 in list(reversed(range(guard_1, len(bananna_counts)))):
				# Make sure things haven't gone wrong
				if guard_2  <= len(bananna_counts)-1 and guard_2 > guard_1 and guard_2 != guard_1:
					# Infinite loops are a good thing.
					# Keep the guards distracted
					if infiniteLoop(bananna_counts[guard_1], bananna_counts[guard_2]):
						# Make sure things haven't gone wrong again
						if 0 <= guard_1 <= len(bananna_counts) and len(bananna_counts) > 0:
							# Remove the guard from the list of guards to parse, and increment the output
							bananna_counts.pop(guard_1)
							output += 1
						if 0 <= guard_2 <= len(bananna_counts) and len(bananna_counts) > 0:
							# Remove the guard from the list of guards to parse, and increment the output
							bananna_counts.pop(guard_2 -1)
							output += 1
	return output

def answer(bananna_counts):
	# Convert to list
	bananna_counts = list(bananna_counts)
	bananna_counts.sort()
	
	# Check edge cases
	for guard in bananna_counts:
		if guard >= 2**30 or guard < 1:
			return 0
	
	# Copy over input to output
	output = []
	for guard in bananna_counts:
		output.append(guard)
	
	# store the number of successfull matches in a list
	successfull_matches = match(bananna_counts)
	
	# Return the number of guards left over
	output = len(output) - successfull_matches
	return output

print(answer([1,1]))