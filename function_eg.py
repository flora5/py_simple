
def avg(first, *rest):
    print rest
    print len(rest)
    return(first + sum(rest))

print avg(10,1,1,1,1)  # rest is a tuple




class A:
    class_attr = 1.0  # class attribute
    __weight = 120 #__private_attrs can not access outside the class

    def print_hello(self): #self must be the first argument
        self.__wight = 300
        print "hello"

    def __init__(self, color,size):
        self.color = color
        self.size = size
        self.__weight = 250 # way to use private attribute inside class
        print "*****",self.class_attr #1.0

    def about_me(self):
        print "Iam %s size is %d, weight is: %d" % (self.__class__, self.size, self.__weight)


a1 = A('green',222)
A.class_attr = 2.0
print a1.class_attr # 2.0 will affected the instance

a1.about_me()

#a1.__weight
#AttributeError: A instance has no attribute '__weight'

# supper

class Parent():
    def __init__(self,name):
        self.name = name
        print self.name

class Child(Parent):
    def __inint__(self,name):
        self.name = name
        print self.name



# meta class




