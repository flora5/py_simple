
"""

A decorator is a function that modifies other functions.

"""

def hello():
    print 'hello'

def decorator(func):
    print "This is decorator "
    func()
    print 'goodbye'
    return func

#hello = decorator(hello)

#syntactic sugar
@decorator
def hello():
    print "hello"





