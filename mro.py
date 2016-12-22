
# super()
"""

"""

class A(object):

	def __init__(self,name):
		self.name = name

	def hello(self):
		pass

# the safe thing to do is to pass the 
#first class in the inheritance list to 
#super unless you know why you want to do something else.

class B():
	def __init__(self,color):
		self.color = color

class C(A,B):
	def __init(self,name,color):
		A.__init__()
		B.__init__()

c = C('sara','yellow')
print(dir(c))

# C, B-A, D 
