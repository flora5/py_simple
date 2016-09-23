import copy

def test(l=[]):

    #l2 =l
    l2 = copy.copy(l)

    l2.append('hello')
    print "l2:",l2
    print "l:",l
    return l



#l =['a']
l =[['a','b'],'c']
print test(l)

