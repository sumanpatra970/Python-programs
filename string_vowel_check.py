#program to check vowel in string
def string():
    k=0
    l=0
    m=0
    n=0
    c=0
    str=input("enter string")
    list=[]
    for i in range(0,len(str)):
         if str[i]=="a" or str[i]=="e" or str[i]=="o" or str[i]=="u" or str[i]=="i":
             list.append(str[i])
    print(list)
    for j in list:
        if j == "a":
            k=k+1
        if j=="i":
            l=l+1
        if j=="e":
            m=m+1
        if j=="o":
            n=n+1
        if j=="u":
            c=c+1

    if k>0 and l>0 and m>0 and n>0 and c>0:
        print("string is ok")
    else:
        print("string is not ok")
string()