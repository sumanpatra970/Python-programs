#program to sort a list in descending order
lst=[1,2,3,4,5]
n=len(lst)
m=n//2
for i in range(0,m+1,1):
    if (lst[i]!=lst[n-1-i]):
        lst[i],lst[n-1-i]=lst[n-1-i],lst[i]
        print(lst)

print("sorting is completed")

