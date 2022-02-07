#string operation with list
list=['apple','ape','lion']
inn=input("enter string")
for i in range(0,1):
    k=inn[i]
    l=inn[i+1]
    print(k,l)
for j in list:
    if j[0]==k and j[1]==l:
        print("element found",j)
    break
else:
    print("no")