

def fun(n, accum):
	if n <= 1:
		return accum
	else:
		return fun(n-1, accum * n)



def countdown(n):
	if n == 0:
		return 
	print n
	countdown(n-1)

countdown(5)
