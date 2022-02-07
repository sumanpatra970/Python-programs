#program to find count of element in array(fixed)
#using logic
import array
k=0
arr=array.array('i',[2,3,5,2,2])
n=2
for i in arr:
    if i==n:
        k=k+1
print(k)
#using function
x=arr.count(2)
print(x)