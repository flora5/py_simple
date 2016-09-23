
"""

A decorator is a function that modifies other functions.
it takes a function as an argument and defines and
 returns a new function that uses the one it was passed


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





