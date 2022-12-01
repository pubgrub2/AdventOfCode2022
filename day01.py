file = open("day01in.txt", "r")
input = file.read().splitlines()
output = []
total = 0
current1 = 0
current2 = 0
current3 = 0
for x in input:
  try:
    total = total + int(x)
  except:
    output.append(total)
    total = 0

for x in output:
  if current1 < x:
    current1 = x

for x in output:
  if current2 < x and x < current1:
    current2 = x

for x in output:
  if current3 < x and x < current2:
    current3 = x

print(current1)
print(current2)
print(current3)
print(current1 + current2 + current3)