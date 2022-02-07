#program of argument
def person(name, *data):
    print(name)
    for i in data:
        person(i)
person('navin','mumbai',95)
