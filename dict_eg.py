d = {'a':1,'b':2,'c':3}
d.items()
#[('a', 1), ('c', 3), ('b', 2)]

d1 = {'a':[1,2],'b':'3','c':4}
d2 = d1.copy()
print d2
d1['a'][0] = 'm'
print d1  #{'a': ['m', 2], 'c': 4, 'b': '3'}
print d2  #{'a': ['m', 2], 'c': 4, 'b': '3'}


a=[1,2,3]
print a[10:]
#[]

seq ={'color','width','size'}
d3 = dict.fromkeys(seq)
print d3
#{'color': None, 'width': None, 'size': None}
d4 = dict.fromkeys(seq,'value')#at most 2 args
print d4
#{'color': 'value', 'width': 'value', 'size': 'value'}
