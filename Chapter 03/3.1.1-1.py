#3.1.1-1.py

"""
File :timing.py
Prints the running times for problem sizs that double.
using a single loop.
"""
import time

problemSize = 10000000
print("%12s%26s" % ("Problem Size", "Seconds"))
for count in range(5):

	start = time.time()
	#the start of rhe algorithm
	work  = 1
	for x in range(problemSize):
		work += 1
		work -= 1
	#The end of the algorithm
	elapsed = time.time() - start

	print("%12s%26s" % (problemSize, elapsed))
	problemSize *=2