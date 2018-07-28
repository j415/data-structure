#3.1.2-1.py

#3.1.1-1.py

"""
File :counting.py
Prints the number of iterations for problem sizes
that double, using a single loop.
"""
import time

problemSize = 1000
print("%12s%26s" % ("Problem Size", "Iterations"))
for count in range(5):
	number = 0
	number1 =0
	#the start of rhe algorithm
	work  = 1
	for j in range(problemSize):
		for k in range(problemSize):
			number += 1
			work += 1
			work -= 1
	#The end of the algorithm
	for l in range(problemSize):
		number1 += 1
		work += 1
		work -= 1

	print("%12s%26s%26s" % (problemSize, number,number1))
	problemSize *=2