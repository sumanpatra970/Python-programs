#program to find fab series upto user-interest
def fab(x):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,x):
        c=a+b;
        a=b
        b=c
        print(c)
n=int(input("enter n"))
fab(n)