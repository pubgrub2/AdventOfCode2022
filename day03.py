input = open("day03.txt").read().splitlines()
output = 0

for x in input:
	string1, string2 = set(x[:len(x)//2]), set(x[len(x)//2:])
	letter = string1.intersection(string2).pop()
	if ord(letter) > 91:
		output += (ord(letter) - 96)
	elif ord(letter) < 91:
		output += (ord(letter) - 38)
	else: print("error processing upper or lower")

print(output)