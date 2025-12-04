from aocd import get_data

data = get_data(day=4, year=2025)
table = [list(row) for row in data.split()]

roll = '@'
empty = '.'

count = 0

directions = [
	(0, 1),  # east
	(0, -1),  # west
	(1, 0),  # north
	(-1, 0),  # south
	(1, 1),  # northeast
	(1, -1),  # northwest
	(-1, 1),  # southeast
	(-1, -1)  # southwest
]

# pad the table with the empty character
padded_table = table.copy()
padded_table.insert(0, [empty] * len(table[0]))
padded_table.append([empty] * len(table[0]))
for i in range(len(padded_table)):
	padded_table[i].insert(0, empty)
	padded_table[i].append(empty)

# check 8 directions, if there is fewer than four rolls, count it as a valid position and continue
for y in range(1, len(padded_table) - 1):
	for x in range(1, len(padded_table[0]) - 1):
		if padded_table[y][x] == roll:
			roll_count = 0
			for direction in directions:
				dx, dy = direction
				try:
					if padded_table[y + dy][x + dx] == roll:
						roll_count += 1
				except IndexError:
					continue
			if roll_count < 4:
				count += 1
print(count)

# part 2
count_two = 0

def remove_rolls(count, table):
	for y in range(1, len(table) - 1):
		for x in range(1, len(table[0]) - 1):
			if table[y][x] == roll:
				roll_count = 0
				for direction in directions:
					dx, dy = direction
					try:
						if table[y + dy][x + dx] == roll:
							roll_count += 1
					except IndexError:
						continue
				if roll_count < 4:
					count += 1
					table[y][x] = empty
	return count, table

prev = -1
table_two = padded_table.copy()
while prev != count_two:
	prev = count_two
	count_two, table_two = remove_rolls(count_two, table_two)
	print(count_two)
print(count_two)