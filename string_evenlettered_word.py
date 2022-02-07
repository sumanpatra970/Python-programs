#string operation to know even lettered word in  a string
str="this is a game show"
dtr1=str.split(" ")
print(dtr1)
for i in range(0,len(dtr1)):
    if len(dtr1[i])%2==0:
        print(dtr1[i])
print("done")

