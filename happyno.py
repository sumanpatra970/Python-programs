#program to find happyno
def happy():
    sum=0
    n=int(input("enter no"))
    m=len(str(n))
    for j in range(0,m+1):
        sum=0
        for i in range(0,m):
            x=n%10
            sum=sum+x**2
            n=n//10
            print(sum)
        n=sum
        print(n)
    if n==100:
        print("it is a happy no")
    else:
        print("not a happy no")
happy()