# Input: positive int
# Output: stingy - genorus
import math

# Custom implementation of itertools.accumulate due to import errors
def accumulate(iterator):
	total = 0
	for item in iterator:
		total += item
		yield total

# Fibonacci Generator
def fibonacci():
	a = 1
	b = 1
	while True:
		yield a
		a, b = b, a + b

def generous(total_lambs):
	return int(math.log(total_lambs + 1, 2.0))

def stingy(total_lambs):
    # Every henchman is given an id and an allowence: id, allowence
    for henchmen_count, henchman_allowence in enumerate(accumulate(fibonacci())):
        # When they start giving out more than they can "afford", its time to stop.
        if henchman_allowence > total_lambs:
            return henchmen_count

def answer(total_lambs):
	# Return the difference
	return stingy(total_lambs) - generous(total_lambs)

print answer(10)