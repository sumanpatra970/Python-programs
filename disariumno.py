#program to find disariumno no
#135 is yes,1^1+3^2+5^3=135
def no():
    sum=0
    n=int(input("enter no"))
    r=n
    m=len(str(n))
    for i in range(m,0,-1):
        x=n%10
        print(x)
        y=n//10
        t=y
        print(y)
        n=t
        sum=sum+x**i
        print(sum)
    if sum==r:
        print("yes disarium no")
    else:
        print("no not a disarium no")
no()
