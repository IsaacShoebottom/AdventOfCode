from aocd import get_data
import re

data = get_data(day=3, year=2024)

def part_one():
	regex = r"mul\((\d+),(\d+)\)"
	matches = re.findall(regex, data, re.MULTILINE)

	total = 0
	for match in matches:
		total += int(match[0]) * int(match[1])
	print(total)

def part_two():
	mul_regex = r"mul\((\d+),(\d+)\)"
	do_str = "do()"
	dont_str = "don't()"

	matches = re.finditer(mul_regex, data, re.MULTILINE)

	total = 0
	for match in matches:
		start = match.start()
		do_match = data.rfind(do_str, 0, start)
		dont_match = data.rfind(dont_str, 0, start)

		if do_match == dont_match == -1: # Neither
			total += int(match.group(1)) * int(match.group(2))
			continue
		if do_match > dont_match: # Do
			total += int(match.group(1)) * int(match.group(2)) # Don't
			continue
		else:
			continue

	print(total)

part_one()
part_two()