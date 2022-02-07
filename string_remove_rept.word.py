#string operations to remove repetated letter from a string
str="geekks"
n=len(str)
newstr=""
for i in range(0,n):
    if str.count(str[i])>1:
        if newstr.count(str[i])>0:
                print(str[i])
        else:
            newstr=newstr+str[i]

    if str.count(str[i])==1:
        newstr=newstr+str[i]

print(newstr)