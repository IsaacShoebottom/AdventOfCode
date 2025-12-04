from aocd import get_data
data = get_data(day=4, year=2024)
table = data.split()
table.reverse()
table = [list(row) for row in table]

def east(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1][x1 + 1] == "M" and table[y1][x1 + 2] == "A" and table[y1][x1 + 3] == "S":
			print(table[y1][x1], table[y1][x1 + 1], table[y1][x1 + 2], table[y1][x1 + 3])
			return True
	except IndexError:
		return False

def west(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1][x1 - 1] == "M" and table[y1][x1 - 2] == "A" and table[y1][x1 - 3] == "S":
			print(table[y1][x1], table[y1][x1 - 1], table[y1][x1 - 2], table[y1][x1 - 3])
			return True
	except IndexError:
		return False

def north(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1 + 1][x1] == "M" and table[y1 + 2][x1] == "A" and table[y1 + 3][x1] == "S":
			print(table[y1][x1], table[y1 + 1][x1], table[y1 + 2][x1], table[y1 + 3][x1])
			return True
	except IndexError:
		return False

def south(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1 - 1][x1] == "M" and table[y1 - 2][x1] == "A" and table[y1 - 3][x1] == "S":
			print(table[y1][x1], table[y1 - 1][x1], table[y1 - 2][x1], table[y1 - 3][x1])
			return True
	except IndexError:
		return False

def northeast(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1 + 1][x1 + 1] == "M" and table[y1 + 2][x1 + 2] == "A" and table[y1 + 3][x1 + 3] == "S":
			print(table[y1][x1], table[y1 + 1][x1 + 1], table[y1 + 2][x1 + 2], table[y1 + 3][x1 + 3])
			return True
	except IndexError:
		return False

def northwest(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1 + 1][x1 - 1] == "M" and table[y1 + 2][x1 - 2] == "A" and table[y1 + 3][x1 - 3] == "S":
			print(table[y1][x1], table[y1 + 1][x1 - 1], table[y1 + 2][x1 - 2], table[y1 + 3][x1 - 3])
			return True
	except IndexError:
		return False

def southeast(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1 - 1][x1 + 1] == "M" and table[y1 - 2][x1 + 2] == "A" and table[y1 - 3][x1 + 3] == "S":
			print(table[y1][x1], table[y1 - 1][x1 + 1], table[y1 - 2][x1 + 2], table[y1 - 3][x1 + 3])
			return True
	except IndexError:
		return False

def southwest(x1, y1):
	try:
		if table[y1][x1] == "X" and table[y1 - 1][x1 - 1] == "M" and table[y1 - 2][x1 - 2] == "A" and table[y1 - 3][x1 - 3] == "S":
			print(table[y1][x1], table[y1 - 1][x1 - 1], table[y1 - 2][x1 - 2], table[y1 - 3][x1 - 3])
			return True
	except IndexError:
		return False

total = 0
for y in range(len(table)):
	for x in range(len(table[y])):
		if east(x, y):
			total += 1
		if west(x, y):
			total += 1
		if north(x, y):
			total += 1
		if south(x, y):
			total += 1
		if northeast(x, y):
			total += 1
		if northwest(x, y):
			total += 1
		if southeast(x, y):
			total += 1
		if southwest(x, y):
			total += 1

print(total)