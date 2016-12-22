

class Node(object):
	pass

class A(node):
	pass

class B(node):
	pass

class C(A,B):
	pass

class Visitor(object):
	def visit(self,node,*args, **kwargs):
		meth = None
		for cls in node.__class__.mro__:
			meth_name = 'visit_' + cls.__name__
			meth = getattr(self,meth_name,None)
			if meth:
				break
		

