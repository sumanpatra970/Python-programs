#program to find harshad no
def harshad():
    n=int(input("enter no"))
    t=n
    sum=0
    for j in range(0,3):
        x=n%10
        n=n//10
        sum=sum+x
        print(sum)
    if t%sum==0:
        print("harshad no",sum)
    else:
        print("not harshad no")
harshad()