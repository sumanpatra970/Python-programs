#string opertaion
str1="geeks for"
str2="learning from geeks for geeks"
list1=str1.split(" ")
list2=str2.split(" ")
for a in range(0,len(list1)):
    for b in range(0,len(list2)):
        if list1[a]==list2[b]:
            break
        else:
            print(list2[b])
for i in list1:
    k=list2.count(i)
    print(k)
    if k >0:
        print ("no")
    else:
        print(i)




