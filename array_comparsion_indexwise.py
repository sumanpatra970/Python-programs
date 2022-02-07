#program to create array by user and comparing element by index
import array
a=array.array('i',[])
n=int(input("enter the length of array"))
for j in range (1,n+1):
    x=int(input("enter value"))
    a.append(x)
b = array.array('i', [])
m = int(input("enter the length of array"))
for i in range(1, m + 1):
        y = int(input("enter value"))
        b.append(y)
print(a)
print(b)
#logic
if n!=m:
    raise Exception('Sorry')
for k in range(0,n):
        if a[k]>b[k]:
            print("a has more value than b for this index")
        elif a[k]<b[k]:
            print("b has more value than a for this index")
        else:
            print("both array has same value at this index")
print("array comparsion is done")

