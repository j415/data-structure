#1.7.5-1.py

import pickle

lyst = [60, "A String object", 1977]
fileObj = open("items.dat", "wb")
for item in lyst:
	pickle.dump(item, fileObj)
fileObj.close()
print(item)