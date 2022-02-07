#program of file handling
y=open("new.txt",'w')
y.write("this is my first class")
y.close()
x=open("new.txt",'r')
for i in x:
    print(i)
