input = open("day03.txt").read().splitlines()
output = 0

def upper_or_lower_output(letter):
	if ord(letter) > 91:
		return((ord(letter) - 96))
	elif ord(letter) < 91:
		return((ord(letter) - 38))
	else: print("error processing upper or lower")

for i in range(0, len(input) - 2, 3):
	string1, string2, string3 = set(input[i]), set(input[i + 1]), set(input[i + 2])
	letter = string1.intersection(string2).intersection(string3).pop()
	output += upper_or_lower_output(letter)

print(output)