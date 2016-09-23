
"""
Iterables
When you create a list, you can read its items one by one.
Reading its items one by one is called iteration:
"""

l = [1,2,3]
for i in l:  #l is an iterable.
    print(i)

# Everything you can use "for... in..." on is an iterable;
# lists, strings, files...
#These iterables are handy because you can read them as
# much as you wish, but you store all the values in memory
# and this is not always what you want when you have a
# lot of values.


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i


mygenerator = create_generator()
print mygenerator
for i in mygenerator:
    print (i)

"""
Generators
Generators are iterators, but you can only iterate over them once.
It's because they do not store all the values in memory,
they generate the values on the fly:

"""

g1 = (x*x for x in range(3))
for i in g1:
    print(i)
#0
#1
#4

for i in g1:
    print(i)
# print nothing
#cannot perform for i in mygenerator a second time
# since generators can only be used once: they calculate 0,
# then forget about it and calculate 1, and end
# calculating 4, one by one.

"""
Yield is a keyword that is used like return,
except the function will return a generator.

1, Insert a line result = [] at the start of the function.
2, Replace each yield expr with result.append(expr).
3, Insert a line return result at the bottom of the function.
4, Yay - no more yield statements! Read and figure out code.
5, Compare function to original definition.

This trick may give you an idea of the logic behind
 the function, but what actually happens with yield is
 significantly different that what happens in the list
 based approach. In many cases the yield approach will be
  a lot more memory efficient and faster too. In other
  cases this trick will get you stuck in an infinite loop,
  even though the original function works just fine. Read
  on to learn more...





"""

