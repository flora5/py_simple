

class A():

	def func1(self):
		print('func1...')

	def func2(self):
		print('func2...')

#m = {'aa': func1, 'bb': func2}


a = A()
c = getattr(a, 'func1',None)
if c:
	c()


