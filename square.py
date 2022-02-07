#program to find sum of square of natural no
n=int(input("enter the no"))
sum=0
for i in (1,n+1):
    sum=i*i+sum
print("sum of square of n no=",sum)