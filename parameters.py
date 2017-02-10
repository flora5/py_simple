
l = []
d = {}
c = 0

def test(l):
	l.append('a')
	d.update({'a': 1})
	c = 10


test(l)
print(l) # ['a']
print(d) # {'a':1}
print(c) # 0