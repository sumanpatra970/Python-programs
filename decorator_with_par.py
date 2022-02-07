#program of decorator using classic call way
def add(func):
    def inner(*args):
        print(args[0]+args[1])
        return func()
    return inner
@add
def info():
   print("we are in info")
a=80
b=90
info(a,b)





