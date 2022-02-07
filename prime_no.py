#program to find prime no in between two nos
a=int(input("enter the strating no"))
b=int(input("enter the ending no"))
for c in range(a,b,1):
    for i in range(2,c):
        if c % i == 0:
            print("no is not prime",c)
            break
        else:
            print("no is prime",c)
            break
print("done")