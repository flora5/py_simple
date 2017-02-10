

from combi import *
perm_space = PermSpace('meow')
print(len(perm_space))
print(perm_space[7])

#Use CombSpace to create a combination space, where order doesn’t matter:
comb_space = CombSpace(('aa','bb','cc'), 2)
print(comb_space)
print(comb_space[2])
print(len(comb_space))