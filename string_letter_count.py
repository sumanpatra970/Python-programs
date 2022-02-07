#program to check same times occurence of two letter in string
def xo(str1):
    k=0
    m=0
    n=len(str1)
    for i in range(0,n):
        if str1[i]== "x":
            k=k+1
        elif str1[i]== "o":
            m+=1
    else:
        print("bye")
    if k==m:
        return True
    else:
        return False
stt=input("enter string")
print(xo(stt))

