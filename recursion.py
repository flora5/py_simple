

import itertools
import sys

l = [1,[2],[3,4,[5,[6,7]]]]

#flattened_list  = list(itertools.chain(*list_of_lists))
#coroutine async/await

def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item


l2 = list(flatten(l))
print(l2)
sys.exit()




def fun(n, accum):
	if n <= 1:
		return accum
	else:
		return fun(n-1, accum * n)



def countdown(n):
	if n == 0:
		return 
	print(n)
	countdown(n-1)

countdown(5)
