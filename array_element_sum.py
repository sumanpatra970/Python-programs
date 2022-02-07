#program to create array by user and sum of elements in array
#user input no fix array
import array
def sum():
    arr=array.array('i',[])
    n=int(input("enter the length of array"))
    for j in range (1,n+1):
        x=int(input("enter value"))
        arr.append(x)
    sum=0
    for i in arr:
        sum=sum+i
    return sum,arr
result=sum()
print(result)


