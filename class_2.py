

# class method, static method, instance method

#  inner working of instance method is the same as the calss method
#  Actually ,python automatically maps an instance method call to a class
# method

#instance.method(args...)
#will be automatically converted to a class method function call like this
# class.method(instance, args...)



#simple method: defined outside of a class.
# this function can access class attributes by feeding instance arg
def outside_foo():
    pass



# self only works inside class
# undefined outside of calss
class A:
    #instance method
    def foo(self):
        pass

    #if we need to use class attributes
    @classmethod
    def class_foo(cls):
        print "This is class method..."

    # do not have any info about the class
    # plain functions except that you can call them from
    # an instance or the class
    #You might want to move a function into a class because it
    # logically belongs with the class
    #you can just use a module function instead of a staticmethod.
    @staticmethod
    def sfoo():
        print "This is static method..."

a1 = A()
a1.class_foo() # two way to call class method/ static method
A.class_foo()

print "--------"
a1.sfoo() #two way to call
A.sfoo()






class A:
    count = 1 # class level variable

    def __init__(self):
        self.count = 2 # object level variable

    def print_hello(self):
        print 'hello'


a = A()

print a.count  #2
print A.count  #1

#A.print_hello() ||error can not call instance function by class




"""
python 2.2 release notes, and it was changed in 2.2.3 to: However,
class methods are still useful in other places, for example, to
program inheritable alternate constructors.
"""

#signle tone
# quick sort
#  container datastructure
