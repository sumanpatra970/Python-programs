#program of sorting array
import array
n=int(input("enter length"))
arr=array.array('i',[])
for x in range(0,n):
    y=int(input("enter value"))
    arr.append(y)
print(arr)
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1-i):
        if arr[j]<arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
        elif arr[j]>arr[j+1]:
            arr[j]=arr[j]
            arr[j+1]=arr[j+1]
print(arr)