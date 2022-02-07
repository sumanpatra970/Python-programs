#program of loop
lis=['ok','ok','ok','ok']
for i in lis:
    if i=='faluty':
        print(f"car is {i}")
        break
    print(f"car is {i}")
else:
    print("all car is ok")
listt= ['ok', 'ok', 'faluty', 'ok']
for j in listt:
    if j == 'faluty':
        print(f"car is {j}")
        break
    print(f"car is {j}")
else:
    print("all car is ok")
student=['suman','rohan','kalia']
for k in student:
    if k=="suman":
        print("suman is present")
        continue
    print(f"my friend is{k}")

