#1.5.3-1.py p19

def factorial(n):
	def recurse(n, product):
		if n==1:
			return product
		else: 
			return recurse(n-1, n * product )
	return recurse(n, 1)
print(factorial(10))

"""def factorial(n, product=1):
	if n==1:
		return product
	else:
		return factorial(n-1, n*product)
print(factorial(5))"""