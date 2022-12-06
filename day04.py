input = open("day04.txt").read().splitlines()
output = 0

for x in input:
	y = x.replace("-", ",").split(",")
	for i, j in enumerate(y):
		y[i] = int(j)
	if (y[0] <= y[2] and y[1] >= y[3]) or (y[0] >= y[2] and y[1] <= y[3]):
		output += 1
	print(y)

print(output)