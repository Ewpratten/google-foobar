# Input: 2D array of "map"
# Output: Shortest distance to exit from cell

# from collections import deque

class deque(object):
	# A custom implementation of collections.deque that is about 2ms faster
    def __init__(self, iterable=(), maxsize=-1):
        if not hasattr(self, 'data'):
            self.left = self.right = 0
            self.data = {}
        self.maxsize = maxsize
        self.extend(iterable)

    def append(self, x):
        self.data[self.right] = x
        self.right += 1
        if self.maxsize != -1 and len(self) > self.maxsize:
            self.popleft()

    def popleft(self):
        if self.left == self.right:
            raise IndexError('cannot pop from empty deque')
        elem = self.data[self.left]
        del self.data[self.left]
        self.left += 1
        return elem

    def extend(self, iterable):
        for elem in iterable:
            self.append(elem)

class Node:
	# A class to represent one wall or hallway
	def __init__(self, x, y, remove_uses=0):
		self.x = x
		self.y = y
		self.remove_uses = remove_uses
	
	# Used by various functions below
	def __iter__(self):
		return iter([self.x, self.y])
	
	def __eq__(self, node):
		return self.x == node.x and self.y == node.y
    
	def __hash__(self):
		return hash(tuple(self))

	# def __str__(self):
	# 	return "({n.x}, {n.y})".format(n=self)

    # def __repr__(self):
    #     return self.__str__()

class Router:
    def __init__(self, matrix, remove_uses):
        self.matrix = matrix
        self.remove_uses = remove_uses
		
		# set the height and width
        self.width = len(matrix[0])
        self.height = len(matrix)
        
        # All possible directions to move in
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        self.visited = set()
        self.distances = {}
    
    def distance(self, start, end):
        # Initalize Variables
        self.distances[start] = 1
        start.remove_uses = self.remove_uses

        # Create double-ended queue
        queue = deque([])
        queue.append(start)

        while queue:
            # Get the first node in the deque
            current_node = queue.popleft()
            self.visited.add(current_node)

            # If the current node is the end, return the distance
            if current_node == end:
                return self.distances[current_node]

            # Check all nodes: Above, Below, Left, and Right
            for adjacent_node in self.getClose(current_node):
                if adjacent_node not in self.visited:
                	# Only move to nodes that havent already been seen
                    self.distances[adjacent_node] = self.distances[current_node] + 1
                    queue.append(adjacent_node)
        # If there is no possible answer, return python's representation of infinity
        return float('inf')
    
    def isWall(self, x, y):
    	# Is it a wall?
        return self.matrix[y][x] == 1

    def getClose(self, node):
    	# Returns all nodes in valid directions around current_node node
        for direction in self.directions:
        	# Get the x and y location of the current_node node
            # print([node.x +direction[0], node.y -direction[0]] )
            x, y = list(tuple(a + b for a, b in zip((node.x, node.y), direction)))
            # Make sure the node is inside the map
            if self.width > x >= 0 and self.height > y >= 0:
            	# Create a class to represent the node at x,y
                adjacent_node = Node(x, y, node.remove_uses)
                if self.isWall(x, y):
                	# Make sure I can still remove more walls
                    if adjacent_node.remove_uses > 0:
                    	# Remove 1 from the number of walls I can take down
                        adjacent_node.remove_uses = adjacent_node.remove_uses - 1
                        yield adjacent_node
                else:
                    yield adjacent_node

    

def answer(input_map):
	
	# Create an object of the map using a router
	# remove_uses = How many walls can I take down?
	# Useless for foobar, just something to play around with
	map_class = Router(input_map, remove_uses=1)

	# Create enterance and exit classes
	enterance_node = Node(0, 0)
	exit_node = Node(map_class.width-1, map_class.height-1)

	# Find the distance between the start and end of the map
	distance = map_class.distance(enterance_node, exit_node)
	
	
	return distance

# print answer([[0,1,1,0],[0,0,0,1],[1,1,0,0],[1,1,1,0]])
for _ in range(0,4):
	print answer([[0, 0, 0, 0, 0, 0],
	             [1, 1, 1, 1, 1, 0],
	             [0, 0, 0, 0, 0, 0],
	             [0, 1, 1, 1, 1, 1],
	             [0, 1, 1, 1, 1, 1],
	             [0, 0, 0, 0, 0, 0]])
