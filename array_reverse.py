#program to reverse array(fix array)
import array
k=0
arr=array.array('i',[2,3,7,8,9])
m=len(arr)
n=m//2
for i in range(0,n):
    if arr[i]!=arr[m-i-1]:
        t=arr[i]
        arr[i]=arr[m-i-1]
        arr[m-i-1]=t
    else:
        break
print(arr)