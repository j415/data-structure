#1.7.4-2.py

f = open("integers.txt", "r")
sum = 0
for line in f:
	wordlist = line.split()
	for word in wordlist:
		number = int(line)
		sum += number
print("The sum is:", sum)