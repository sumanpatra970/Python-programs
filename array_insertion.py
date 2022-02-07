import array
n=int(input("enter size"))
a=[None]*(n+1)
for j in range(n):
    x=int(input("enter element"))
    a[j]=x
print(a)
m=int(input("enter the index no"))
k=int(input("data you want to insert"))
for i in range(n-1,-1,-1):
    if i>=m:
        a[i+1]=a[i]
    if i+1==m:
        a[i+1]=k
        break
print(a)