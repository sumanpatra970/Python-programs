#program to use dictionary in fstring
student={'rolf':23, 'ket':22, 'sim':24 }
for info in student:
    print(info)
for info_details in student.items():
    print(info_details)
for name,age in student.items():
    print(f"my friend is {name} and his age is {age}")

