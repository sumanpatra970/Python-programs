str="suman"
newstr=""
n=len(str)
print(str[3])
for i in range(n,0,-1):
    newstr=newstr+str[i-1]
    print(newstr)
str=newstr
print("string after reverse="+newstr)