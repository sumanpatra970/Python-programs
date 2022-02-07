#program to know common letters in two given string
str1="abcdef"
str2="iuycab"
k=0
for i in range(0,len(str1),1):
        if str2.count(str1[i])>0:
                k=k+1
        else:
                break
print("no of common letter in both the strings are",k)