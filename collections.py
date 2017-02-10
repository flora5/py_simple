#-*- coding: utf-8 -*-

"""
collections 的功能不错，如果用瞄一眼就可以，
但是要面试....看几遍都忘...所以说没事不要随便换工作

"""


import collections

ct = collections.Counter()
for word in ['red', 'blue','red','green','blue','red']:
    ct[word] += 1

print(ct)
#sum(some_counter.values())
