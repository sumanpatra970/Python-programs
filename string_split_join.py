#program of split and join in string
str=input("enter string")
str1=str.split("/")
str2=""
for i in str1:
    str2=str2+i

str3="-".join(str2)
print(str3)
str4="0".join(str1)
print(str4)
