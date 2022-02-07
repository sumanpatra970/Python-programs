#program to calculate factorial of a no
def fac(x):
    f=1
    for i in range(1,x+1):
            f=f*i
    print(f)
n=int(input("enter no"))
fac(n)