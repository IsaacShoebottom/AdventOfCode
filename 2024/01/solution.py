from aocd import get_data
data = get_data(day=1, year=2024)

# Condition data
list1 = []
list2 = []
lines = data.split("\n")
for line in lines:
	nums = line.split("   ")
	num1 = int(nums[0])
	num2 = int(nums[1])
	list1.append(num1)
	list2.append(num2)
list1.sort()
list2.sort()

# Part 1
total_dist = 0
for i in range(len(list1)):
	dist = list2[i] - list1[i]
	dist = abs(dist)
	total_dist += dist

print("Total distance: ", total_dist)

# Part 2
total_similarity = 0
for i in range(len(list1)):
	num = list1[i]
	occurs = 0
	for j in range(len(list2)):
		if num == list2[j]:
			occurs += 1
	similarity = num * occurs
	total_similarity += similarity

print("Total similarity: ", total_similarity)