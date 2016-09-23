#-*- coding:utf-8 -*-

"""
所有内建类型都是类. int(), type(), list() 等是工厂函数
看上去像函数，实际是类

"""





class A():
    version = 0.1 # static variable
    def __init__(self,nm='flora'):
        #constructor
        self.name = nm
        """初始化一个名为name的类实例属性/成员,这个变量只存在于类实例中
        它并不是实际类本身的一部分
        __init__()方法会在类实例创建完之后自动执行，

        """

    def showname(self):
        #display instance attribute and class name
        print "name is:", self.name
        print self.__class__.__name__

    def showver(self):
        #display class(static) attribute
        print self.version

    def addMe2Me(self,x):
        return x+x



class A1:
    def __init__(self):
        print "initialized..."
    def instance_id(self):
        print id(self)

a1 = A1()

print a1.instance_id()
print id(a1)




