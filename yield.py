

# Generator don't hold the entire result in memory 
# it yeild one result at a time
# a big list or file

def step():
	return '001'
	return '002'
	return '003'


s = step()
for i in [0,0,0]:
	print(s)


def step2():
	yield '111'
	yield '222'
	yield '333'

s2 = step2()
#for i in [0,0,0]:
#	print(s2.next()) 
print(s2.__next__()) #111
print(next(s2))  #222
print(s2.__next__())  #333

#g.next() has been renamed to g.__next__()


def count_down(num):
	while num > 0:
		yield num
		num -= 1

c = count_down(10)
for i in range(10):
	print(c.__next__())



#--------------------------------------------
def do_stuff(val):
    yield val + 3
    yield val + 10

my_gen = do_stuff(0)

print(next(my_gen))
print(next(my_gen))

# range xrange
#xrange() was renamed to range() in Python 3.
# list iterator

l = ['a','b','c']
a = iter(l)
for i in range(3):
	print(a.__next__())



def square(nums):
	for i in nums:
		yield (i*i+1000)

n1 = square([11,12,13,14])
print(next(n1))
print(next(n1))


def fun(num):
	print(num + 100)

eval('func(11)') # 111






