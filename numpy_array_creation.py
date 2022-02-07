import numpy
n=int(input("enter the row"))
m=int(input("enter column"))
arr=numpy.zeros((n, m))
for i in range(n):
    for j in range(m):
        x: int=int(input("enter element"))
        arr[i][j]=x
for i in range(n):
    for j in range(m):
        print(arr[i][j])

arrr=[int]*2
print(len(arrr))
arrr2=numpy.zeros((2))
print(len(arrr2))
arrr.append(2)
print(arrr)
