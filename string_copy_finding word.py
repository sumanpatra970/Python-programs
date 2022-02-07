#program of copying string and finding word in string
str="sumanpatra"
test=""
for i  in range(0,len(str),1):
    if i !=2:
        test=test+str[i]
print(test)
print(len(str))
s1="me"
s2="geeks for me"
s3=s2.split(" ")
print(s3)
for k in s3:
    if k==s1:
        print("yes")
    else:
        print("no")


