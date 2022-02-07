#program to know no of vowels in a string(fix)
str="geaels"
k=0
for i in range(0,len(str)):
    if str[i]=="a" or str[i]=="e" or str[i]=="o" and str[i]=="i" or str[i]=="u":
        k=k+1
print("no of vowel is",k)