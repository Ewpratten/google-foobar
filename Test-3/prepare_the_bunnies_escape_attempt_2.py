# Input: 2D array of "map"
# Output: Shortest distance to exit from cell

# Revision 2 with help from my python book and some documentation

class deque(object):
	# A custom implementation of collections.deque that is about 0.4s faster
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
    def __init__(self, x, y, remove_uses, hallway_map):
        # X, Y, number of walls I can take down, the entire map
        self.x = x
        self.y = y
        self.remove_uses = remove_uses
        self.hallway_map = hallway_map

    def __eq__(self, comp):
        return self.x == comp.x and self.y == comp.y and self.remove_uses == comp.remove_uses

    def __hash__(self):
        return self.x + len(self.hallway_map) * self.y

    def getClosest(self):
        # Return all surounding nodes
        
        # Location of current node
        x = self.x
        y = self.y
        
        # Initalize Vars
        vertices = []
        remove_uses = self.remove_uses
        hallway_map = self.hallway_map
        width = len(hallway_map[0])
        height = len(hallway_map)

        # Make sure that notes are not placed beyond the walls
        if x > 0:
            wall = hallway_map[y][x - 1] == 1
            if wall:
                if remove_uses > 0:
                    # Subtract from number of wals I can take down until I have run out of walls
                    vertices.append(Node(x - 1, y, remove_uses - 1, hallway_map))
                else:
                    pass
            else:
                # Do nothing if the node is a hallway
                vertices.append(Node(x - 1, y, remove_uses, hallway_map))
                
        # The exact same thing for all other walls below:
        
        if x < width - 1:
            wall = hallway_map[y][x + 1] == 1
            if wall:
                if remove_uses > 0:
                    vertices.append(Node(x + 1, y, remove_uses - 1, hallway_map))
                else:
                    pass
            else:
                vertices.append(Node(x + 1, y, remove_uses, hallway_map))

        if y > 0:
            wall = hallway_map[y - 1][x] == 1
            if wall:
                if remove_uses > 0:
                    vertices.append(Node(x, y - 1, remove_uses - 1, hallway_map))
                else:
                    pass
            else:
                vertices.append(Node(x, y - 1, remove_uses, hallway_map))

        if y < height - 1:
            wall = hallway_map[y + 1][x]
            if wall:
                if remove_uses > 0:
                    vertices.append(Node(x, y + 1, remove_uses - 1, hallway_map))
                else:
                    pass
            else:
                vertices.append(Node(x, y + 1, remove_uses, hallway_map))

        # Return all touching nodes
        return vertices


class PathFinder:
    def __init__(self, hallway_map, remove_uses):
        # New path finder
        self.hallway_map = hallway_map
        self.height = len(hallway_map)
        self.width = len(hallway_map[0])
        self.remove_uses = remove_uses # Number of walls I can take down

    def getShortestPath(self):
        # Use breadth-first search
        
        start = Node(0, 0, self.remove_uses, self.hallway_map)
        # Create a double-ended queue
        queue = deque([start])
        distances = {start: 1}

        while queue:
            # Get the next node from the deque
            current_node = queue.popleft()

            # If the current_node location happens to be the exit, return the distance
            if current_node.x == self.width - 1 and current_node.y == self.height - 1:
                return distances[current_node]

            # If not at end of maze, add some more nodes
            for neighbor in current_node.getClosest():
                if neighbor not in distances.keys():
                	# Add next node to the deque
                    distances[neighbor] = distances[current_node] + 1
                    queue.append(neighbor)


def answer(input_map):
	# Create an object of the map using a Path Finder
	# 1 = How many walls can I take down?
	# Useless for foobar, just something to play around with
    router = PathFinder(input_map, 1)
    # The most important part
    return router.getShortestPath()

# Used to debug
# for _ in range(0,4):
# 	print answer([[0, 0, 0, 0, 0, 0],
# 	             [1, 1, 1, 1, 1, 0],
# 	             [0, 0, 0, 0, 0, 0],
# 	             [0, 1, 1, 1, 1, 1],
# 	             [0, 1, 1, 1, 1, 1],
# 	             [0, 0, 0, 0, 0, 0]])