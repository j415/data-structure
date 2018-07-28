#1.7.4-1.py

f = open ("integers.txt", "r")
sum = 0
for line in f:
	line = line.strip()
	number =int(line)
	sum += number
print("The sum is", sum)