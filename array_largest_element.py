#program to find largest element in array(fixed)
from array import array
n=int(input("enter length"))
val=array('i',[])
for x in range(0,n):
    y=int(input("enter value"))
    val.append(y)
print(val)
lar=val[0]
for i in range(0,n,1):
    if i==n-1:
        if val[i] > lar:
            lar = val[i + 1]
            print(lar)
        else:
            lar=lar
            print(lar)
    else:
        if val[i+1]>lar:
            lar=val[i+1]
            print(lar)
        else:
            lar=lar
            print(lar)
print("largest value in array is=",lar)