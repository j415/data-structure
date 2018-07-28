#1.7.5-2.py

import pickle

lyst = list()
fileObj = open("items.dat","rb")
while True:
	try:
		item = pickle.load(fileObj)
		lyst.append(item)
	except EOFError:
		fileObj.close()
		break
print(lyst)