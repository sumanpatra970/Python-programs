#program to know presence of 0 and 1 in a string(fix)
str="0101"
n=len(str)
k=0
for i in range(0,len(str)):
    if str[i]=="0" or str[i]=="1":
        k=k+1
if k==n:
    print("yes",k)
else:
    print("no",k)