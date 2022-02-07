#what is monotonic array-array element is either increasing or decreasing
#program to know monotonic array or not
import array
def arr():
    n = int(input("enter length"))
    arr = array.array('i', [])
    for x in range(0, n):
        y = int(input("enter value"))
        arr.append(y)
    print(arr)
    k=1
    if arr[0]>arr[1]:
        for i in range(0,n-1,1):
            if arr[i]>arr[i+1] or arr[i]==arr[i+1]:
                k+=1
            else:
                break
    else:
        for i in range(0,n-1,1):
            if arr[i]<arr[i+1] or arr[i]==arr[i+1]:
                k+=1
            else:
                break
    if k==n:
        print("monotonic")
    else:
        print("not monotonic")

arr()