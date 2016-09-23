


def f1(l):
    l.append('hello')
    return l

def f2(l):
    tmp = list(l) #create a new list
    #If the list contains more references,deepcopy()
    tmp.append('hello')
    return tmp


l = []
print f1(l)  #['hello']
print l  # ['hello']

l2 =[]
print '-------------'
print f1(l2[:]) #['hello']
print l2 # []


print '---------------'
l1 = []
print f2(l1) # ['hello']
print l1  # []


l3 = [1,2,3,4]
l4 = [1,2]
diff_list = list(set(l3) - set(l4))
print diff_list
#[3,4]
