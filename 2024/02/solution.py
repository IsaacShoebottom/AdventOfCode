file = open("input.txt", "r").read()
lines = file.split("\n")
reports = []
for line in lines:
	nums = line.split(" ")
	nums = [int(num) for num in nums]
	reports.append(nums)

total_safe = 0
safe_nums = [1, 2, 3]

for report in reports:
	dists = [report[i+1] - report[i] for i in range(len(report)) if i != len(report) - 1]
	# dists is either all positive or all negative (checks all increasing or all decreasing)
	if all([dist > 0 for dist in dists]) or all([dist < 0 for dist in dists]):
		dists = [abs(dist) for dist in dists]
	if all([dist in safe_nums for dist in dists]):
			total_safe += 1

print("Total safe reports: ", total_safe)

total_safe_tolerance = 0
for report in reports:
	print("Checking report: ", report)
	dists = [report[i+1] - report[i] for i in range(len(report)) if i != len(report) - 1]
	for i in range(len(dists)):
		if abs(dists[i]) not in safe_nums:
			report_copy = report.copy()
			report_copy.pop(i+1)
			dists_copy = [report_copy[i+1] - report_copy[i] for i in range(len(report_copy)) if i != len(report_copy) - 1]
			if all([dist > 0 for dist in dists_copy]) or all([dist < 0 for dist in dists_copy]):
				dists_copy = [abs(dist) for dist in dists_copy]
			if all([dist in safe_nums for dist in dists_copy]):
				print("Popping (dist): ", report[i+1])
				report.pop(i+1)
			else:
				print("Popping (dist): ", report[i])
				report.pop(i)
			break
	else:
		# make a list comprehension that makes the list a 0 if its negative and a 1 if its positive and then if the sum is 1 or len(dists) - 1 then its safe
		lst = [0 if dist < 0 else 1 for dist in dists]
		if sum(lst) == 1: # Only one positive
			for i in range(len(report)):
				if dists[i] > 0:
					report_copy = report.copy()
					report_copy.pop(i+1)
					dists_copy = [report_copy[i+1] - report_copy[i] for i in range(len(report_copy)) if i != len(report_copy) - 1]
					if all([dist > 0 for dist in dists_copy]) or all([dist < 0 for dist in dists_copy]):
						dists_copy = [abs(dist) for dist in dists_copy]
					if all([dist in safe_nums for dist in dists_copy]):
						print("Popping (asce): ", report[i+1])
						report.pop(i+1)
					else:
						print("Popping (asce): ", report[i])
					report.pop(i)
					break
		elif sum(lst) == len(dists) - 1: # Only one negative
			for i in range(len(report)):
				if dists[i] < 0:
					report_copy = report.copy()
					report_copy.pop(i+1)
					dists_copy = [report_copy[i+1] - report_copy[i] for i in range(len(report_copy)) if i != len(report_copy) - 1]
					if all([dist > 0 for dist in dists_copy]) or all([dist < 0 for dist in dists_copy]):
						dists_copy = [abs(dist) for dist in dists_copy]
					if all([dist in safe_nums for dist in dists_copy]):
						print("Popping (desc): ", report[i+1])
						report.pop(i+1)
					else:
						print("Popping (desc): ", report[i])
					report.pop(i)
					break
	dists = [report[i+1] - report[i] for i in range(len(report)) if i != len(report) - 1]
	# dists is either all positive or all negative (checks all increasing or all decreasing)
	if all([dist > 0 for dist in dists]) or all([dist < 0 for dist in dists]):
		dists = [abs(dist) for dist in dists]
	if all([dist in safe_nums for dist in dists]):
			print("Safe report: ", report)
			total_safe_tolerance += 1

print("Total safe reports with tolerance: ", total_safe_tolerance)