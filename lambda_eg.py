
f = lambda x,y,z: x+y+z
print f(1,2,3) # 1+2+3 = 6


f1 = lambda x,y,z: x+y+x
print f1(1,2,3) #1+2+1 = 4


a = ['e','f','g']
f2 = lambda x: x*2
print map(f2,a) # ['ee', 'ff', 'gg']

