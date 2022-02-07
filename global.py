i=2
x=90
def show():
    x=80
    global i
    print(i)
    y=globals()['x']
    print(x+y)
show()
print(i)
