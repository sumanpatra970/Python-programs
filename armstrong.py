#program to check whether no is armstrong or not
no=int(input("enter the no"))
temp=no
sum=0
while (no>=1):
    i=no%10
    no=no//10
    sum=i*i*i+sum
print(sum)
if sum==temp:
    print("no is armstrong no")
else:
    print("no is not armstrong")