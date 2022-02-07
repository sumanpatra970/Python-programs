#program to find element in list
lst=[4,5,7,6,9]
a=int(input("enter no"))
for i in range (1,len(lst)):
    if lst[i]==a:
        print("element exist")
        break
else:
    print("element doesnot exist")
