"""
filter(function or None, sequence) -> list, tuple, or string
Return those items of sequence for which function(item) is true.  If
    function is None, return the items that are true.  If sequence is a tuple
    or string, return the same type, else return a list.

"""

str = ['a','b','c','d']

def func(s):
    if s!='a':
        return s
    else:
        return None

print filter(func,str) #['b', 'c', 'd']

a = [1, 2, 3]
b = [4, 5, 6, 7]
c = [8, 9, 1, 2, 3]
L = map(lambda x: len(x), [a, b, c])
# L == [3, 4, 5]


"""
reduce(...)
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
"""

# L == [3, 4, 5]

N = reduce(lambda x, y: x+y, L) # 3+4  +5
# N == 12

