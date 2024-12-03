from aocd import get_data
import re

data = get_data(day=3, year=2024)

# Part one
matches = re.findall(r"mul\((\d+),(\d+)\)", data)
total = 0
for match in matches:
	total += int(match[0]) * int(match[1])
print(total)

# One-liner
# print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", data)))

# Part two
matches = re.finditer(r"mul\((\d+),(\d+)\)", data)
total = 0
for match in matches:
	start = match.start()
	do_match = data.rfind("do()", 0, start)
	dont_match = data.rfind("don't()", 0, start)
	if do_match == dont_match == -1: # Neither
		total += int(match.group(1)) * int(match.group(2))
	elif do_match > dont_match: # Do
		total += int(match.group(1)) * int(match.group(2))
print(total)