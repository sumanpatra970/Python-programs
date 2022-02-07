#program of decorator using @function
user="suman"
def outer(func):
    def inner():
        if user=="suman":
            return func()
    return inner()
@outer
def super():
    print("acess is granted by user")
