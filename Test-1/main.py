def parse(data):
	return {x:data.count(x) for x in data}

def answer(data,n):
	counts = parse(data)
	banlist = []
	returndata = []
	
	for number in counts:
		if counts[number] > n:
			banlist.append(number)
	
	for number in data:
		if number not in banlist:
			returndata.append(number)
	print(returndata)

answer([1,2,3], 6)