# Input: 2d matrix of state probabilities
# Output: list of neumerators and a denominator

def getGCD(a,b):
    if (b == 0):
        return a
    else:
        return getGCD(b, a % b)

def getGCDList(matrix):
	# Returns the greatest common denominator of a list (or matrix)
    legnth = len(matrix)
    output = 0
    for i in range(0, legnth):
        output = getGCD(output, matrix[i])
    return output

def fuse(matrix, row, col):
	
    # Get the size of the data passed in
    row_legnth=len(matrix[row])
    col_legnth=sum(matrix[col])
    
    # Get the indices
    indices=(set(range(row_legnth))-{row,col})
    
    # Create a new blank matrix of the same width as the origional matrix
    output_matrix = [0 for i in matrix[row]]
    
    # Iterate through every index
    for i in indices:
    	# Populate the new matrix using back propagated distribution
        output_matrix[i]= col_legnth*matrix[row][i]+matrix[row][col]*matrix[col][i]
        
    # Get greatest common denominator
    gc=getGCDList(output_matrix)
    
    # Return a list of GCDs
    output = [int( i / gc ) for i in output_matrix ]
    return output

def answer(m):
	# Find the size
	height = len(m)
	width = len(m[0])
	
	# Duplicate m for modification
	matrix = list(m)
	
	# Clear the matrix
	for i,form in enumerate(matrix):
		form[i] = 0
	
	# Get the sum of each state's probability
	state_sums = []
	for state in matrix:
		state_sums.append(sum(state))
	
	# Find all terminal states, then store them in a list
	terminal_states = [i for i,item in enumerate(state_sums) if item==0]
	
	# Find all non-terminal states, then store them in a list
	nonterminal_states = list((set(range(height)) - set(terminal_states)))
	
	# How many non-terminal states are there?
	nonterminal_states_count = len(nonterminal_states)
	
	# Iterate through each non-terminal state
	for i in range(0, nonterminal_states_count - 1):
		index_col = nonterminal_states[ nonterminal_states_count -i -1 ]
		# Iterate through each probability
		for j in range(0, nonterminal_states_count -1):
			index_row = nonterminal_states[j]
			# Replace matrix with new generated data
			matrix[index_row] = fuse( matrix, index_row, index_col)
	output = []
	for i in terminal_states:
		output.append(matrix[0][i])
	
	# append the base tothe end of the list
	total = sum(output)
	output.append(total)
	
	if not total:
		# Fill output with 1
		output = [1 for i in terminal_states]
		output.append(len(terminal_states))
	
	return output



# mat=[
#         [1, 2, 3, 0, 0, 0],
#         [4, 5, 6, 0, 0, 0],
#         [7, 8, 9, 1, 0, 0],
#         [0, 0, 0, 0, 1, 2],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]
        
#     ]

# print answer(mat)