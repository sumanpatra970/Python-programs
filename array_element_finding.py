#program to create array by user and find the element
#user created array
from array import *
arr=array('i',[])
n=int(input("enter the length of array"))
for i in range(n):
    x=int(input("enter the next value"))
    arr.append(x)
print(arr)
val=int(input("enter the value"))
#finding index of element
for j in range(n):
    if arr[j]==val:
        print("yes value is found in",j)
        c = arr.index(val)
        print("val is found in array at ", c)
        break
else:
    print("no value is not found in array")

