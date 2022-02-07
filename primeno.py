#program to know prime  no or not
a=int(input("enter the no"))
for i in range(2,a):
    if a%i == 0:
        print("no is not prime")
    else:
         print("no is prime")
         break