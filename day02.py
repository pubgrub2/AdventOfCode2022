input = open("day02.txt").read().splitlines()
score = 0
for x in input:
	if x[0] == "A":
		enemy = 1
	elif x[0] == "B":
		enemy = 2
	elif x[0] == "C":
		enemy = 3
	if x[2] == "X":
		friendly = 1
	elif x[2] == "Y":
		friendly = 2
	elif x[2] == "Z":
		friendly = 3
	if enemy == friendly:
		score = score + friendly + 3
	elif enemy + 1 == friendly or enemy - 2 == friendly:
		score = score + friendly + 6
	elif enemy == friendly + 1 or enemy == friendly - 2:
		score = score + friendly

print(score)