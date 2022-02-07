#use of continue in string
str="suman"
newstr=""
k="u"
for i in range(0,len(str)):
    if str[i]==k:
        continue
    else:
        newstr=newstr+str[i]
print(newstr)
