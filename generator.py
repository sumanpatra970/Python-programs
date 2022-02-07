#program of generator
def new():
    for i in range(3):
        sq=i*i
        yield sq

values=new()
print(next(values))
print(next(values))
print(next(values))


